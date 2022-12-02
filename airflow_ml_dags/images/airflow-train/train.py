import os
import pickle

import click
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer


@click.command('train')
@click.option('--input-dir', type=click.Path())
@click.option('--output-dir', type=click.Path())
def train(input_dir: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    X = pd.read_csv(os.path.join(input_dir, 'X_train.csv'))
    y = pd.read_csv(os.path.join(input_dir, 'y_train.csv'))
    numerical_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    categorical_features = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']

    numerical_pipeline = Pipeline([
        ("impute", SimpleImputer()),
        ("scale", StandardScaler())
    ])

    categorical_pipeline = Pipeline([
        ("impute", SimpleImputer(strategy="most_frequent")),
        ("ohe", OneHotEncoder(handle_unknown="ignore"))
    ])

    transformer = ColumnTransformer([
        ("num_transformer",
         numerical_pipeline,
         numerical_features),
        ("cat_transformer",
         categorical_pipeline,
         categorical_features)
    ])

    model = Pipeline([
        ("transformer", transformer),
        ("model", LogisticRegression())
    ])
    model.fit(X, y)

    with open(os.path.join(output_dir, 'model.pkl'), 'wb') as f:
        pickle.dump(model, f)


if __name__ == '__main__':
    train()
