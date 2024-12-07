from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def filter_demo(df, config):
    columns_to_remove = config['filters']['f0-demo']['columns_to_remove']
    for column in columns_to_remove:
        df = df.drop(column)
    return df