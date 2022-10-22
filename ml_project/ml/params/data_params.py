from dataclasses import dataclass, field


@dataclass()
class DataParams:
    input_data_path: str = field(default="data/train.csv")
