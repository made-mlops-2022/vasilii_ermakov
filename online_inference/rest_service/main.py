import os
import pickle

import pandas as pd
from fastapi import FastAPI
from fastapi_health import health
import gdown

from rest_service.schemas import Data

app = FastAPI(title="Heart disease detection")
model = None


@app.on_event("startup")
def prepare_model():
    global model
    if os.path.exists("model1.pkl"):
        with open("model1.pkl", 'rb') as f:
            model = pickle.load(f)
    else:
        url_to_model = os.getenv("URL_TO_MODEL")
        gdown.download(url_to_model, "model1.pkl", fuzzy=True)
        with open("model1.pkl", 'rb') as f:
            model = pickle.load(f)


@app.post(
    "/predict",
    response_description="Does patient have a heart disease",
    description="Predict if patient have a heart disease",
)
async def predict(data: Data):
    X = pd.DataFrame([data.dict()])
    y = model.predict(X)
    return {"disease": bool(y[0])}


def check():
    return model is not None


app.add_api_route('/health', health([check]))
