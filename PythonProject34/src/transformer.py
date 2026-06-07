from pyspark.sql.functions import col, when, upper, lower

from src.mapping import column_mapping


def remove_duplicates(df, config):
    try:
        if (config["transformations"]["dropDuplicates"]):
            df = df.dropDuplicates()
            return df
    except Exception as e:
        print("Error while dropdup", e)

#
# def columnbmapping(df, config):
#     try:
#         if (config["transformations"]["column_mapping"]):
#             for old, new in column_mapping.items():  # ❌ also: 'column_mapping' is undefined!
#                 df = df.withColumn(old, new)
#             return df   # ✅ only returns here
#     except Exception as e:
#         print("error while mapping ", e)
#     # ❌ No return outside the if — returns None!

# def columnbmapping(df,config):
#      try:
#          if (config["transformations"]["column_mapping"]):
#              for old,new in config["transformations"]["column_mapping"].items():
#                  df = df.withColumnRenamed(old,new)
#              return df
#      except Exception as e:
#          print("error while mapping ",e)
#          return df

def columnbmapping(df, config):
    try:
        if (config["transformations"]["column_mapping"]):
            for old, new in config["transformations"]["column_mapping"].items():
                df = df.withColumnRenamed(old, new)
            return df
    except Exception as e:
        print("error while mapping ", e)
        return df




def transformed(df, config):
    try:
        df = remove_duplicates(df, config)
        df = columnbmapping(df, config)
        return df

    except Exception as e:
        print(" Error in Transformation")
        print(e)