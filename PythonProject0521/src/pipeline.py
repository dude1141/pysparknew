"""Pipeline orchestrator — coordinates extract, transform, load."""
import sys
import os

# Allow running pipeline.py directly from PyCharm
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pyspark.sql import SparkSession
from src.reader import read_data
from src.transformer import transform_data
from src.writer import write_data
from src.utils import load_config


class Pipeline:
    def __init__(self, config: dict):
        self.config = config
        self.name = config["pipeline"]["name"]
        self.env = config["pipeline"]["environment"]
        self.spark_config = config.get("spark_config", {})

    def _build_spark(self) -> SparkSession:
        builder = SparkSession.builder.appName(f"{self.name}_{self.env}")
        for key, value in self.spark_config.items():
            builder = builder.config(key, value)
        return builder.getOrCreate()

    def validate(self):
        assert self.name, "Pipeline must have a name"
        assert self.config.get("source"), "Source config required"
        assert self.config.get("target"), "Target config required"
        print(f"Pipeline '{self.name}' validated successfully.")

    def execute(self):
        print(f"\n{'='*50}")
        print(f"Pipeline '{self.name}' starting (env={self.env})")
        print(f"{'='*50}")
        spark = self._build_spark()

        try:
            print("\n--- RAW DATA ---")
            df = read_data(spark, self.config)
            df.show(truncate=False)

            print("\n--- TRANSFORMED DATA ---")
            df = transform_data(df, self.config)
            df.show(truncate=False)

            write_data(df, self.config)
            print(f"\nPipeline '{self.name}' completed successfully.")
            print(f"{'='*50}\n")
        except Exception as e:
            print(f"Pipeline '{self.name}' failed: {e}")
            raise
        finally:
            spark.stop()


if __name__ == "__main__":
    config_path = os.path.join(os.path.dirname(__file__), "..", "config", "dev.yaml")
    config = load_config(config_path)
    Pipeline(config).execute()
