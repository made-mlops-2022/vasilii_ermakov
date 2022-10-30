import logging
import os.path
import pickle
import unittest

import pandas as pd
from sklearn.pipeline import Pipeline

from ml import pipeline
from ml import predict
from ml.params.pipeline_params import read_pipeline_params
from ml.model.model import Model
from ml.data.data import Data
import generate_data


def suppress_logging(func):
    def wrapper(self, *args, **kwargs):
        logging.disable(logging.INFO)
        func(self, *args, **kwargs)
    return wrapper


class MLTests(unittest.TestCase):
    @suppress_logging
    def test_pipeline(self):
        pipeline.run_train_pipeline("configs/train_config.yaml")
        self.assertTrue(os.path.isfile("metrics/metrics.json"))
        self.assertTrue(os.path.isfile("models/model1.pkl"))

    @suppress_logging
    def test_model(self):
        params = read_pipeline_params("configs/train_config.yaml")
        data = Data(
            params.input_data_path, params.splitting_params, params.feature_params
        )
        model = Model(params.model_params, params.feature_params)
        self.assertIsNone(model.prediction)
        self.assertIsInstance(model.pipeline, Pipeline)
        model.train(data.get_train_features(), data.get_train_target())
        model.predict(data.get_test_features())
        self.assertIsNotNone(model.prediction)
        self.assertListEqual(
            list(model.evaluate(data.get_test_target()).keys()),
            ["accuracy", "precision", "recall", "roc_auc"]
        )
        self.assertEqual(model.serialize(
            params.output_solution), "models/model1.pkl"
        )

    @suppress_logging
    def test_another_model(self):
        params = read_pipeline_params("configs/train_config_2.yaml")
        data = Data(
            params.input_data_path, params.splitting_params, params.feature_params
        )
        model = Model(params.model_params, params.feature_params)
        self.assertIsNone(model.prediction)
        self.assertIsInstance(model.pipeline, Pipeline)
        model.train(data.get_train_features(), data.get_train_target())
        model.predict(data.get_test_features())
        self.assertIsNotNone(model.prediction)
        self.assertListEqual(
            list(model.evaluate(data.get_test_target()).keys()),
            ["accuracy", "precision", "recall", "roc_auc"]
        )
        self.assertEqual(model.serialize(
            params.output_solution), "models/model1.pkl"
        )

    @suppress_logging
    def test_wrong_config(self):
        with self.assertRaises(NotImplementedError):
            params = read_pipeline_params("tests/wrong_config.yaml")
            _ = Data(
                params.input_data_path, params.splitting_params, params.feature_params
            )
            _ = Model(params.model_params, params.feature_params)

    @suppress_logging
    def test_wrong_order(self):
        with self.assertRaises(ValueError):
            params = read_pipeline_params("configs/train_config.yaml")
            data = Data(
                params.input_data_path, params.splitting_params, params.feature_params
            )
            model = Model(params.model_params, params.feature_params)
            model.train(data.get_train_features(), data.get_train_target())
            model.evaluate(data.get_test_target())

    def test_generated_data(self):
        generate_data.generate()
        params = read_pipeline_params("tests/train_generated_data.yaml")
        data = Data(
            params.input_data_path, params.splitting_params, params.feature_params
        )
        model = Model(params.model_params, params.feature_params)
        self.assertIsNone(model.prediction)
        self.assertIsInstance(model.pipeline, Pipeline)
        model.train(data.get_train_features(), data.get_train_target())
        model.predict(data.get_test_features())
        self.assertIsNotNone(model.prediction)
        self.assertListEqual(
            list(model.evaluate(data.get_test_target()).keys()),
            ["accuracy", "precision", "recall", "roc_auc"]
        )
        self.assertEqual(model.serialize(
            params.output_solution), "models/model1.pkl"
        )

    @suppress_logging
    def test_predict(self):
        with open("models/model1.pkl", "rb") as file:
            model = pickle.load(file)
        features = pd.read_csv("data/test.csv")
        predict.predict(model, features, "predictions/predict.csv")
        self.assertTrue(os.path.isfile("predictions/predict.csv"))
        predict.predict(model, features, "predictions/my_predict.csv")
        self.assertTrue(os.path.isfile("predictions/my_predict.csv"))


if __name__ == "__main__":
    unittest.main()
