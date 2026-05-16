from pyspark.sql import SparkSession
from pyspark.sql.functions import col, coalesce, when
from pyspark.sql.types import StructType, StructField, StringType

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, coalesce
from pyspark.sql.types import StructType, StructField, StringType
spark = SparkSession.builder.appName("hi").getOrCreate()


data1= [(1,"kiran",26),(3,"ally",76),(4,"tomrhy",44)]
schema= ["id","name","age"]
df= spark.createDataFrame(data1,schema)
df.show()


transactions = (
 (1, 1000),
 (2, 200),
 (3, 5000)
)
schema= ["transactionsid","amount"]

df3= spark.createDataFrame(transactions,schema)

# df3.show()
# How would you add a new column category with values "High" if amount is greater than
# 1000, "Medium" if amount is between 500 and 1000, and "Low" otherwise?
try:
    def functions(df):
        return df.withColumn("Category",when(col("amount") > 1000, "High")
                    .when((col("amount") > 500) & (col("amount") <= 1000), "Medium")
                    .otherwise("Low"))


    df4 = functions(df3)
    df4.show()

except Exception as e:
    print(e)
finally:
    print("i am finally")




--------------+------+--------+
|transactionsid|amount|Category|
+--------------+------+--------+
|             1|  1000|  Medium|
|             2|   200|     Low|
|             3|  5000|    High|
+--------------+------+--------+

i am finally
