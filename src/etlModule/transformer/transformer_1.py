from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def add_amount_col(df: DataFrame, config) -> DataFrame:
    return df.withColumn('amount', col('price') * col('quantity'))

def add_derived_col(df, etl_config):
    transformation = etl_config['transformations']['t0-demo']
    if transformation == 'multiply_by_2':
        df = df.withColumn("price_multiple_2", col('price') * 2)
    elif transformation == 'add_10':
        df = df.withColumn(etl_config['price_add_10'], col('price') + 10)
    return df