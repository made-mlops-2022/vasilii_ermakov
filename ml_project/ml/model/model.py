import pickle
from typing import Dict

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import (
    accuracy_score, roc_auc_score, precision_score, recall_score
)

from ml.params.model_params import ModelParams
from ml.params.feature_params import FeatureParams


class Model:
    def __init__(
            self, model_params: ModelParams, feature_params: FeatureParams
    ) -> None:
        self.prediction = None
        model_type = model_params.model_type
        if model_type == "LogisticRegression":
            model = LogisticRegression()
        elif model_type == "KNeighborsClassifier":
            model = KNeighborsClassifier()
        else:
            raise NotImplementedError()

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
             feature_params.numerical_features),
            ("cat_transformer",
             categorical_pipeline,
             feature_params.categorical_features)
        ])

        self.pipeline = Pipeline([
            ("transformer", transformer),
            ("model", model)
        ])

    def train(self, features: pd.DataFrame, target: pd.Series) -> None:
        self.pipeline.fit(features, target)

    def predict(self, features: pd.DataFrame) -> None:
        self.prediction = self.pipeline.predict(features)

    def evaluate(self, y_true: pd.Series) -> Dict[str, float]:
        if self.prediction is None:
            raise ValueError("Must predict before evaluate")

        return {
            "accuracy": accuracy_score(y_true, self.prediction),
            "precision": precision_score(y_true, self.prediction),
            "recall": recall_score(y_true, self.prediction),
            "roc_auc": roc_auc_score(y_true, self.prediction)
        }

    def serialize(self, output: str) -> str:
        with open(output, "wb") as file:
            pickle.dump(self.pipeline, file)
        return output
