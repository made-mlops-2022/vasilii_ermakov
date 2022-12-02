import os
import pickle

import click
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


@click.command('validate')
@click.option('--validation-dir', type=click.Path())
@click.option('--model-dir', type=click.Path())
@click.option('--output-dir', type=click.Path())
def validate(validation_dir: str, model_dir: str, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    X = pd.read_csv(os.path.join(validation_dir, 'X_test.csv'))
    y_true = pd.read_csv(os.path.join(validation_dir, 'y_test.csv'))

    with open(os.path.join(model_dir, 'model.pkl'), 'rb') as f:
        model = pickle.load(f)

    y_pred = model.predict(X)
    accuracy = accuracy_score(y_true, y_pred)
    with open(os.path.join(output_dir, 'metrics.txt'), 'w') as f:
        f.write(f'Accuracy: {accuracy}')


if __name__ == '__main__':
    validate()