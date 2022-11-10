import logging
import sys

import pickle
import click
import pandas as pd
from sklearn.pipeline import Pipeline


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def predict(model: Pipeline, features: pd.DataFrame, output_path: str) -> None:
    prediction = pd.Series(model.predict(features))
    prediction.to_csv(output_path)
    logger.info(f"prediction was written to {output_path}")


@click.command(name="predict")
@click.argument("path_to_features")
@click.argument("path_to_model")
@click.option("-o", default="predictions/predict.csv", show_default=True)
def predict_command(
        path_to_features: str,
        path_to_model: str,
        o: str) -> None:
    with open(path_to_model, "rb") as f:
        model = pickle.load(f)
    features = pd.read_csv(path_to_features)
    predict(model, features, o)


if __name__ == "__main__":
    predict_command()
