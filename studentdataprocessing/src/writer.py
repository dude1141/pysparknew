def write_data(df,config):
    try:
        df.write \
            .format(config["target"]["format"]) \
            .option("header", config["target"]["header"]) \
            .mode(config["target"]["mode"]) \
            .option("path", config["target"]["outputpath"]) \
            .save()
        return df
    except Exception as e:
        print("Error in writing ")
        print(e)