import os
import pickle

import click
import gdown
import pandas as pd


@click.command('predict')
@click.option('--data-dir', type=click.Path())
@click.option('--model-dir', type=click.Path())
@click.option('--prediction-dir', type=click.Path())
@click.option('--link', type=str)
def predict(data_dir: str, model_dir: str, prediction_dir: str, link: str):
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(model_dir, exist_ok=True)
    os.makedirs(prediction_dir, exist_ok=True)
    path_to_model = os.path.join(model_dir, "model.pkl")
    gdown.download(link, path_to_model, fuzzy=True)
    with open(path_to_model, 'rb') as f:
        model = pickle.load(f)
    X = pd.read_csv(os.path.join(data_dir, "train_data.csv"))
    y = pd.DataFrame(model.predict(X))
    y.to_csv(os.path.join(prediction_dir, 'predictions.csv'), index=False)


if __name__ == "__main__":
    predict()
