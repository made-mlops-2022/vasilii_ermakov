from dataclasses import dataclass

from marshmallow_dataclass import class_schema
import yaml

from ml.params.feature_params import FeatureParams
from ml.params.splitting_params import SplitParams
from ml.params.model_params import ModelParams


@dataclass()
class PipelineParams:
    input_data_path: str
    output_solution: str
    output_metrics: str
    splitting_params: SplitParams
    model_params: ModelParams
    feature_params: FeatureParams


PipelineParamsSchema = class_schema(PipelineParams)


def read_pipeline_params(path: str) -> PipelineParams:
    with open(path, "r", encoding="UTF-8") as config_file:
        schema = PipelineParamsSchema()
        return schema.load(yaml.safe_load(config_file))
