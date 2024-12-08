
def write_to_database(df, db_config):
    # Write the DataFrame to the database table
    df.write \
        .format("jdbc") \
        .option("url", db_config["url"]) \
        .option("driver", db_config["driver"]) \
        .option("dbtable", db_config["table"]) \
        .option("user", db_config["user"]) \
        .option("password", db_config["password"]) \
        .mode("overwrite") \
        .save()