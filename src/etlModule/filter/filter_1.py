from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def filter_demo(df, filter_config):
    columns_to_remove = filter_config.get('columns_to_remove', [])
    #df = df.drop(*columns_to_remove)
    for column in columns_to_remove:
        df = df.drop(column)
    return df