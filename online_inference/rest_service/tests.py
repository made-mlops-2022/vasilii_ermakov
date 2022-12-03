import json

import pytest
from fastapi.testclient import TestClient

from rest_service.main import app, prepare_model


@pytest.fixture()
def init_model():
    prepare_model()


def test_predict():
    request = {
        'age': 69,
        'sex': 1,
        'cp': 0,
        'trestbps': 160,
        'chol': 234,
        'fbs': 1,
        'restecg': 2,
        'thalach': 131,
        'exang': 0,
        'oldpeak': 0.1,
        'slope': 1,
        'ca': 1,
        'thal': 0
    }
    with TestClient(app) as client:
        response = client.post("/predict", json=request)
        assert response.status_code == 200
        assert response.json() == {"disease": True}


def main():
    test_predict()


if __name__ == "__main__":
    main()
