"""Data sink writers."""
from abc import ABC, abstractmethod


class Sink(ABC):
    @abstractmethod
    def write(self, df):
        pass


class ParquetSink(Sink):
    def __init__(self, config: dict):
        self.path = config["target"]["output_path"]
        self.mode = config["target"]["mode"]

    def write(self, df):
        df.write.mode(self.mode).parquet(self.path)


def write_data(df, config: dict):
    target_format = config["target"]["format"].lower()
    sinks = {"parquet": ParquetSink}

    if target_format not in sinks:
        raise ValueError(f"Unsupported sink format: {target_format}")

    sink = sinks[target_format](config)
    sink.write(df)
    print(f"Data written to {config['target']['output_path']} successfully")
