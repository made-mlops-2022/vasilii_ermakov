import os

import numpy as np
import pandas as pd
import click


SIZE = 100
NAME_OF_GENERATED_DATA = "generated_data.csv"


@click.command('generate-data')
@click.option('--output-dir', type=click.Path())
def generate_data(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    generate(output_dir)

    data = pd.read_csv(os.path.join(output_dir, NAME_OF_GENERATED_DATA))
    target = data['condition']
    features = data.drop('condition', axis=1)

    features.to_csv(os.path.join(output_dir, 'data.csv'), index=False)
    target.to_csv(os.path.join(output_dir, 'target.csv'), index=False)


def generate(path: str) -> None:
    data = {}
    data["age"] = pd.Series(np.random.randint(18, 91, size=SIZE))
    data["sex"] = pd.Series(np.random.randint(0, 2, size=SIZE))
    data["cp"] = pd.Series(np.random.randint(0, 4, size=SIZE))
    data["trestbps"] = pd.Series(np.random.randint(94, 201, size=SIZE))
    data["chol"] = pd.Series(np.random.randint(126, 565, size=SIZE))
    data["fbs"] = pd.Series(np.random.randint(0, 2, size=SIZE))
    data["restecg"] = pd.Series(2 * np.random.randint(0, 2, size=SIZE))
    data["thalach"] = pd.Series(np.random.randint(71, 203, size=SIZE))
    data["exang"] = pd.Series(np.random.randint(0, 2, size=SIZE))
    data["oldpeak"] = pd.Series(6.2 * np.random.random(size=SIZE))
    data["slope"] = pd.Series(np.random.randint(0, 3, size=SIZE))
    data["ca"] = pd.Series(np.random.randint(0, 3, size=SIZE))
    data["thal"] = pd.Series(np.random.randint(0, 3, size=SIZE))
    data["condition"] = pd.Series(np.random.randint(0, 2, size=SIZE))
    df = pd.DataFrame(data)
    df.to_csv(f"{path}/{NAME_OF_GENERATED_DATA}", index=False)


if __name__ == "__main__":
    generate_data()
