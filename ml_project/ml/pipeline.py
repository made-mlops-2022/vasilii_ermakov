import json

import click

from ml.params.pipeline_params import read_pipeline_params
from ml.data.data import Data
from ml.model.model import Model


def run_train_pipeline(config_path: str):
    params = read_pipeline_params(config_path)
    data = Data(
        params.input_data_path, params.splitting_params, params.feature_params
    )
    pipeline = Model(params.model_params, params.feature_params)
    pipeline.train(data.get_train_features(), data.get_train_target())
    pipeline.predict(data.get_test_features())
    metrics = pipeline.evaluate(data.get_test_target())

    with open(params.output_metrics, "w") as metrics_file:
        json.dump(metrics, metrics_file)

    path_to_model = pipeline.serialize(params.output_solution)


@click.command(name="pipeline")
@click.argument("config_path")
def train_pipeline_command(config_path: str):
    run_train_pipeline(config_path)


if __name__ == "__main__":
    train_pipeline_command()