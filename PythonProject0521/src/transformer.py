"""Transformation steps for the customer ETL pipeline."""
from pyspark.sql.functions import col, upper


def drop_duplicates(df, config: dict):
    if config["transformations"].get("drop_duplicates"):
        df = df.dropDuplicates()
    return df


def uppercase_columns(df, config: dict):
    cols = config["transformations"].get("uppercase_columns", [])
    for c in cols:
        df = df.withColumn(c, upper(col(c)))
    return df


def filter_salary(df, config: dict):
    salary_threshold = config["transformations"]["filter_condition"]["salary"]
    return df.filter(col("salary") >= salary_threshold)


def transform_data(df, config: dict):
    df = drop_duplicates(df, config)
    df = uppercase_columns(df, config)
    df = filter_salary(df, config)
    print(f"Transformations applied — {df.count()} rows remaining")
    return df
