import os

import click
import pandas as pd
from sklearn.model_selection import train_test_split


@click.command('split')
@click.option('--input-dir', type=click.Path())
@click.option('--train-dir', type=click.Path())
@click.option('--validation-dir', type=click.Path())
def split_data(input_dir: str, train_dir: str, validation_dir: str):
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(validation_dir, exist_ok=True)
    data = pd.read_csv(os.path.join(input_dir, 'train_data.csv'))
    target = pd.read_csv(os.path.join(input_dir, 'target.csv'))

    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=123)
    X_train.to_csv(os.path.join(train_dir, 'X_train.csv'), index=False)
    y_train.to_csv(os.path.join(train_dir, 'y_train.csv'), index=False)
    X_test.to_csv(os.path.join(validation_dir, 'X_test.csv'), index=False)
    y_test.to_csv(os.path.join(validation_dir, 'y_test.csv'), index=False)


if __name__ == "__main__":
    split_data()
