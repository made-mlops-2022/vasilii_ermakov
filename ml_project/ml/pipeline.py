import json
import logging
import sys

import click

from ml.params.pipeline_params import read_pipeline_params
from ml.data.data import Data
from ml.model.model import Model

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def run_train_pipeline(config_path: str):
    logger.info(f"running pipeline with configs on path: {config_path}")
    params = read_pipeline_params(config_path)
    logger.info("collecting data...")
    data = Data(
        params.input_data_path, params.splitting_params, params.feature_params
    )
    logger.info("done")
    pipeline = Model(params.model_params, params.feature_params)
    logger.info("training pipeline...")
    pipeline.train(data.get_train_features(), data.get_train_target())
    logger.info("done")
    pipeline.predict(data.get_test_features())
    metrics = pipeline.evaluate(data.get_test_target())
    logger.info(f"metrics: {metrics}")
    logger.info(f"metrics have been written to {params.output_metrics}")

    with open(params.output_metrics, "w") as metrics_file:
        json.dump(metrics, metrics_file)

    path_to_model = pipeline.serialize(params.output_solution)
    logger.info(f"model have been written to {path_to_model}")


@click.command(name="pipeline")
@click.argument("config_path")
def train_pipeline_command(config_path: str):
    run_train_pipeline(config_path)


if __name__ == "__main__":
    train_pipeline_command()
