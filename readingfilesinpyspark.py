from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# ---------------------------
# Spark Session
# ---------------------------

class readingfilesinpyspark :

    def __init__(self):

        self.spark= SparkSession.builder \
            .appName("test") \
            .master("local[*]") \
            .getOrCreate()

        self.schema1 = StructType ([StructField("id", IntegerType()),
                                  StructField("name", StringType()),
                                  StructField("Salary", IntegerType()),
                                  StructField("City", StringType()
                                              )])

        #self.schema! and self.spark are isntance variables and can be accessed any where in spark

    def main(self):
        try:
            data = r"C:\Users\mouni\Downloads\details-2026-04-051.csv"


            df = self.spark.read.format("csv") \
              .option("header", True) \
              .option("MODE", "DROPMALFORMED") \
              .schema(self.schema1).load(data)
            df.printSchema()

            def funct(df):
                return df.select(
                    col("id"),
                    col("name"),
                    col("salary"),
                    col("city"),
                    when(col("salary") > 1000, "RICH").otherwise("POOR").alias("status"))

            # funct(df)
            df2 = funct(df)
            df.createOrReplaceTempView("tempview")
            print("df21")
            df2.show(20)

        except Exception as e:
            print(e)
        finally:
            print("i am finally")


if __name__ == "__main__":
    app = readingfilesinpyspark()
    app.main()



