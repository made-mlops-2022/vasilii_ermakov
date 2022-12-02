from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
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


with DAG(
    'generate_data',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2022, 11, 17)
) as dag:
    generate_data = DockerOperator(
        image='airflow-generate-data',
        command='--output-dir /data/raw/{{ ds }}',
        network_mode='bridge',
        task_id='docker-airflow-generate-data',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=DATA_DIR, target='/data', type='bind')]
    )

    generate_data
