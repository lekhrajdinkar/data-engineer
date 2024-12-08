from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def add_amount_col(df: DataFrame, config) -> DataFrame:
    return df.withColumn('amount', col('price') * col('quantity'))

def transformation_1(df: DataFrame, transformations: dict):
    # Apply multiplication transformations
    if 'multiply' in transformations:
        for transform in transformations['multiply']:
            col_name = transform['onCol']
            factor = transform['factor']
            mode = transform['mode']
            if mode == 'new_col':
                df = df.withColumn(f"{col_name}_multiplied_by_{factor}", col(col_name) * factor)
            elif mode == 'same_col':
                df = df.withColumn(col_name, col(col_name) * factor)

    # Apply addition transformations
    if 'add' in transformations:
        for transform in transformations['add']:
            col_name = transform['onCol']
            factor = transform['factor']
            mode = transform['mode']
            if mode == 'new_col':
                df = df.withColumn(f"{col_name}_added_by_{factor}", col(col_name) + factor)
            elif mode == 'same_col':
                df = df.withColumn(col_name, col(col_name) + factor)

    return df
