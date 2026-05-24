from datetime import date

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, coalesce, when, avg, split, count, length
from pyspark.sql.types import StructType, StructField, StringType, DateType, TimestampType, datetime, IntegerType

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, coalesce
from pyspark.sql.types import StructType, StructField, StringType
spark = SparkSession.builder.appName("hi").getOrCreate()

from pyspark.sql import functions as F
data1= [(1,"kiran",26),(3,"ally",76),(4,"tomrhy",44)]
schema= ["id","name","age"]
df= spark.createDataFrame(data1,schema)
# df.show()


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
    # df4.show()

except Exception as e:
    print(e)
finally:
    print("i am finally")


from pyspark.sql.functions import col, lit, regexp_substr, regexp_replace, regexp_extract

a= "abc1234cde678"

df = spark.createDataFrame([(a,)], ["value"])

# df.select(regexp_extract(col("value"),"([0-9]+)([a-z]+)", 1)).show() #case sensitive




schema = StructType([
    StructField("user_id",     StringType(), False),
    StructField("email",       StringType(), True),
    StructField("signup_date", DateType(),   True),
    StructField("last_login",  DateType(),   True),
])

# Data
data = [
    ("U001", "john.doe@gmail.com",    date(2024, 1,  1),  date(2024, 3,  1)),
    ("U002", "jane.smith@outlook.com", date(2024, 2, 15),  date(2024, 3, 10)),
    ("U003", "alice.jones@yahoo.org",  date(2024, 3,  1),  date(2024, 3, 20)),
]

df = spark.createDataFrame(data, schema=schema)
# df1.show()

def extractfun(df):
    df = df.select(col("*"),regexp_extract(col("email"),"(@[A-Za-z.]+)", 1).alias("new"))
    df = df.filter(df.new.endswith("org"))
    df = df.select(avg(
    F.datediff(col("last_login"), col("signup_date"))).alias("avg_days_to_last_login"))
    return df


try:
    df =extractfun(df)
except Exception as e:
    print("e...",e)

from datetime import datetime


schema3 = StructType([
    StructField("sessionid",     StringType(), False),
    StructField("url",       StringType(), True),
    StructField("timestamps", TimestampType(),   True),
    StructField("user_agent",  StringType(),   True),
])

# Data
data = [
    ("S001", "https://example.com/home",    datetime(2024, 7, 1, 10,  0,  0),'Chrome/90.0'),
    ("S002", "http://sample.org/contact", datetime(2024, 7, 2, 11, 30,  0), 'Firefox/85.0'),
    ("S003", "https://example.com/admin", datetime(2024, 7, 3, 12, 45,  0), 'Safari/14.1'),]

df21 = spark.createDataFrame(data, schema=schema3)

# df21.show()

def extractfun1(df21):
    df21 = df21.withColumn("protocol", split(col("url"), "://").getItem(0))
    df21 = df21.withColumn("domain", split(split(col("url"), "://").getItem(1), "/").getItem(0))
    df21 = df21.withColumn("path", split(split(col("url"), "://").getItem(1), "/").getItem(1))
    df21 = df21.filter(~col("path").startswith("admin"))
    df21 = df21.groupBy("domain").agg(avg(length(col("path"))).alias("avg_path_length"),count("*").alias("session_count")).dropDuplicates()
    return df21

try:
    df21 =extractfun1(df21)
    # df21.show(truncate=False)
except Exception as e:
    print("e...",e)


schema2 = StructType([
    StructField("order_id",       StringType(),  False),
    StructField("order_date",     DateType(),    True),
    StructField("delivery_date",  DateType(),    True),
    StructField("product_id",     StringType(),  True),
    StructField("quantity",       IntegerType(), True),
    StructField("price_per_unit", IntegerType(), True),
])

data1 = [
    ("O001", date(2024, 12,  1), date(2024, 12, 10), "P001", 10, 15),
    ("O002", date(2024, 12,  2), date(2024, 12,  8), "P002",  5, 20),
    ("O003", date(2024, 12,  5), date(2024, 12, 15), "P003",  8, 25),
]

df_orders = spark.createDataFrame(data1, schema=schema2)

df_orders.show(truncate = False)
# /*
# Problem: You have a DataFrame user_logins with columns: login_id, user_id, login_timestamp,
# activity_type, and session_duration.
# Use date_format to extract the month and day of the week from login_timestamp.
# Extract the hour of the day from login_timestamp using hour.
# Filter logins where activity_type contains "purchase" and session_duration exceeds 1 hour.
# Group by user_id and day_of_week and calculate:
# The total session_duration per user per day of the week.
# The count of logins per user per day of the week.
# */
from pyspark.sql import functions as sf
def extractfun1(df_orders):
    df_orders = df_orders.withColumn("extratMonthyear", sf.date_format('order_date', 'MM-yyyy'))
    df_orders = df_orders.withColumn("extractYear", sf.date_format('order_date', 'yyyy'))
    df_orders = df_orders.filter(sf.datediff(col('delivery_date'), col('order_date'))> 5)
    df_orders = df_orders.groupBy("extratMonthyear").agg(sf.sum(col("quantity")).alias("totalqty"),
     sf.sum(col("quantity")*col("price_per_unit")).alias("total_revenue")).dropDuplicates()

    return df_orders

try:
    df_logins =extractfun1(df_orders)
    df_logins.show(truncate=False)
except Exception as e:
    print("e...",e)


