import os
from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.python import PythonSensor
from airflow.models import Variable
from airflow.utils.email import send_email_smtp
from docker.types import Mount


DATA_DIR = Variable.get('DATA_DIR')


def failure_callback(context):
    dag_run = context.get('dag_run')
    subject = f'DAG {dag_run} has failed'
    send_email_smtp(to=default_args['email'], subject=subject)


default_args = {
    'owner': 'vasilii_ermakov',
    'email': ['vasya.ermakov.2001@mail.ru'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'on_failure_callback': failure_callback,
}


def wait_for_file(file_name):
    return os.path.exists(file_name)


with DAG(
    'train',
    default_args=default_args,
    schedule_interval='@weekly',
    start_date=datetime(2022, 11, 18)
) as dag:
    wait_data = PythonSensor(
        task_id='wait-for-data',
        python_callable=wait_for_file,
        op_args=['/opt/airflow/data/raw/{{ ds }}/data.csv'],
        timeout=10000,
        poke_interval=10,
        retries=1000,
        mode="poke"
    )

    preprocess = DockerOperator(
        image='airflow-preprocess',
        command='--input-dir /data/raw/{{ ds }} --output-dir /data/processed/{{ ds }}',
        network_mode='bridge',
        task_id='docker-airflow-preprocess',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=DATA_DIR, target='/data', type='bind')]
        )

    split = DockerOperator(
        image='airflow-train-test-split',
        command='--input-dir /data/processed/{{ ds }} --train-dir /data/train/{{ ds }} --validation-dir /data/val/{{ ds }}',
        network_mode='host',
        task_id='docker-airflow-train-test-split',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=DATA_DIR, target='/data', type='bind')]
    )

    train = DockerOperator(
        image='airflow-train',
        command='--input-dir /data/train/{{ ds }} --output-dir /data/models/{{ ds }}',
        network_mode='host',
        task_id='docker-airflow-train',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=DATA_DIR, target='/data', type='bind')]
    )

    validate = DockerOperator(
        image='airflow-validate',
        command='--validation-dir /data/val/{{ ds }} --model-dir /data/models/{{ ds }} --output-dir /data/metrics/{{ ds }}',
        network_mode='host',
        task_id='docker-airflow-validate',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=DATA_DIR, target='/data', type='bind')]
    )

    wait_data >> preprocess >> split >> train >> validate
