from utils import load_config
from reader import read_data
from transformer import transformed  # fixed typo: transfomer -> transformer
from writer import write_data
from pyspark.sql import SparkSession
import sys
import os
try:
    spark = SparkSession.builder \
        .appName("studentdata") \
        .getOrCreate()

    config = load_config("C:/Users/mouni/PycharmProjects/PythonProject34/config/dev.yaml")

    df = read_data(spark,config)

    finaldf = transformed(df, config)

    finaldf.show(truncate =False)


    # write_data(finaldf, config)

except Exception as e:
    print("exception ", e)
finally:
    if 'spark' in locals():
        spark.stop()