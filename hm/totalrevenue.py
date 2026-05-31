# Calculating the percentage contribution of each product's revenue to the total revenue in its
# catego

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as sums
from pyspark.sql.window import Window

data2 = [
    ("Product1", "Category1", 100),
    ("Product2", "Category1", 200),
    ("Product3", "Category1", 150),
    ("Product4", "Category2", 300),
    ("Product5", "Category2", 250),
    ("Product6", "Category2", 180)
]
schemas2 = ["Product", "Category", "Revenue"]

spark = SparkSession.builder.appName("hi").getOrCreate()
df = spark.createDataFrame(data2, schemas2)

windowspec2 = Window.partitionBy("Category")

totalrevencatdf = df.select( "*",sums(col("Revenue")).over(windowspec2).alias("totalrevenuebycat"))

totalrevencatdf.show(truncate=False)


# %percentage contribution

percetagedf = totalrevencatdf.select("*",col("Revenue")/col("totalrevenuebycat")* 100).alias("percentagerev")

percetagedf.show(truncate=False)