import os
import sys
import logging

import requests
import click
import pandas as pd


@click.command(name="make_requests")
@click.option("--ip", default="127.0.0.1")
@click.option("--port", default="8000")
def main(ip, port):
    logger = logging.getLogger("Fake Requests")
    handler = logging.StreamHandler(sys.stdout)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    path_to_data = "generated_data.csv"
    if not os.path.exists(path_to_data):
        path_to_data = "make_requests/generated_data.csv"
    df = pd.read_csv(path_to_data).drop("condition", axis=1)
    fake_requests = df.to_dict(orient="records")

    for request in fake_requests:
        response = requests.post(
            f"http://{ip}:{port}/predict",
            json=request
        )
        logger.info(f"Status code {response.status_code}")
        logger.info(f"Disease: {response.json()}")


if __name__ == "__main__":
    main()
