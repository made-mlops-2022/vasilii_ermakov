import pandas as pd
from sklearn.model_selection import train_test_split

from ml.params.splitting_params import SplitParams
from ml.params.feature_params import FeatureParams


class Data:
    def __init__(
            self, path: str, split_params: SplitParams, feature_params: FeatureParams
    ) -> None:
        self.data = pd.read_csv(path)
        self.numerical_features = feature_params.numerical_features
        self.categorical_features = feature_params.categorical_features
        self.target_feature = feature_params.target_feature[0]
        self.train_data, self.test_data = train_test_split(
            self.data, test_size=split_params.test_size, random_state=split_params.random_state
        )

    def get_train_features(self) -> pd.DataFrame:
        return self.train_data[
            self.categorical_features + self.numerical_features
        ]

    def get_train_target(self) -> pd.Series:
        return self.train_data[self.target_feature]

    def get_test_features(self) -> pd.DataFrame:
        return self.test_data[
            self.categorical_features + self.numerical_features
        ]

    def get_test_target(self):
        return self.test_data[self.target_feature]
