import sys
import os

def read_data(spark,config):
    try:
        df = spark.read \
            .format(config["source"]["format"]) \
            .option("header", config["source"]["header"]) \
            .option("inferSchema", config["source"]["inferSchema"]) \
            .option("path", config["source"]["file_path"]) \
            .load()
        return df

    except Exception as e:
        print("error while reading")
        print(e)