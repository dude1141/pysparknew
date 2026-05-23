from pyspark.sql.functions import col, when, upper, lower

def remove_duplicates(df, config):
    try:
        if (config["transformations"]["dropDuplicates"]):
            df = df.dropDuplicates()
            return df
    except Exception as e:
        print("Error while dropdup", e)


def upper_case_conv(df, config):
    try:
        if (config["transformations"]["upper_case_columns"]):
            df = df.withColumn("name", upper(col("name")))
            return df
    except Exception as e:
        print("Error while upper_case_conv", e)


def lowercase_columns(df, config):
    try:
        if (config["transformations"]["lowercase_columns"]):
            df = df.withColumn("course", lower(col("course")))
            return df
    except Exception as e:
        print("Error while lowercase_columns", e)


def startswith_data(df, config):
    try:
        start_col = config["transformations"]["startswith"]["column"]
        start_val = config["transformations"]["startswith"]["value"]
        df = df.filter(col(start_col).startswith(start_val))  # use config values
        return df
    except Exception as e:
        print("Error while startswith_data", e)
    return None

def endswithinfo(df, config):
    try:
        cols = config["transformations"]["endswith"]["column"]
        endval = config["transformations"]["endswith"]["value"]
        df = df.filter(col(cols).endswith(endval))  # use config values
        print("gmail")
        df.show()
        return df
    except Exception as e:
        print("Error while endswithinfo", e)
    return None

def filtermarks(df, config):
    try:
        # start_col = config["transformations"]["filter_marks"]["marks"]
        # start_val = config["transformations"]["startswith"]["value"]
        df = df.withColumn("grade", when(col("marks") > 80,'A' )
                           . when(col("marks") > 60,'B')
                            .otherwise("C"))
        print("df..")
        df.show()

        # df = df.filter(col(start_col).startswith(start_val))  # use config values
        return df
    except Exception as e:
        print("Error while startswith_data", e)
    return None

def totalmarks(df, config):
    try:
        # start_col = config["transformations"]["filter_marks"]["marks"]
        # start_val = config["transformations"]["startswith"]["value"]
        df = df.withColumn("totalmarks", col("marks")+10)
        print("df.marks.")
        df.show()

        # df = df.filter(col(start_col).startswith(start_val))  # use config values
        return df
    except Exception as e:
        print("Error while totalmarks", e)
    return None

def transformed(df, config):
    try:
        df = remove_duplicates(df, config)
        df = lowercase_columns(df, config)
        df = startswith_data(df, config)
        df = upper_case_conv(df, config)
        df = filtermarks(df,config)
        df = totalmarks(df,config)
        df = endswithinfo(df,config)
        return df

    except Exception as e:
        print(" Error in Transformation")
        print(e)