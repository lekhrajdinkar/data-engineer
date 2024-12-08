from etlModule.transformer.transformer_1 import transformation_1
from pyspark.sql import DataFrame


def apply_transformations(df: DataFrame, transformations: dict):
    df = transformation_1(df, transformations)
    # df = transformation_2(df, transformations)
    # df = transformation_3(df, transformations)
    # ...
    return df
