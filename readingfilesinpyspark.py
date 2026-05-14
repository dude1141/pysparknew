from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# ---------------------------
# Spark Session
# ---------------------------
spark = SparkSession.builder \
    .appName("test") \
    .master("local[*]") \
    .getOrCreate()
data = r"C:\Users\mouni\Downloads\details-2026-04-05.csv"
schema1 = StructType ([StructField ("id", IntegerType()),
                        StructField ("name", StringType()),
                      StructField("Salary", IntegerType()),
                StructField("city", StringType())
                      ])
df =spark.read.format("csv").option("header","True").option("mode","DROPMALFORMED").schema(schema1).load(data)
df.printSchema()
df.show(100)
