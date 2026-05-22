"""Data source reader."""
from abc import ABC, abstractmethod


class Source(ABC):
    @abstractmethod
    def read(self):
        pass


class CSVSource(Source):
    def __init__(self, config: dict, spark):
        self.spark = spark
        self.path = config["source"]["file_path"]
        self.header = config["source"]["header"]
        self.infer_schema = config["source"]["inferSchema"]

    def read(self):
        return (
            self.spark.read
            .format("csv")
            .option("header", self.header)
            .option("inferSchema", self.infer_schema)
            .load(self.path)
        )


def read_data(spark, config: dict):
    source_format = config["source"]["format"].lower()
    sources = {"csv": CSVSource}

    if source_format not in sources:
        raise ValueError(f"Unsupported source format: {source_format}")

    source = sources[source_format](config, spark)
    df = source.read()
    print(f"Data loaded successfully — {df.count()} rows")
    return df
