from pyspark.sql import DataFrame

from pyspark.sql import functions as F

def validate_data(df: DataFrame) -> DataFrame:
    # Check for null values in critical columns
    critical_columns = ['id', 'fund', 'price', 'quantity']
    df = df.filter(~F.col('id').isNull())
    df = df.filter(~F.col('fund').isNull())
    df = df.filter(~F.col('price').isNull())
    df = df.filter(~F.col('quantity').isNull())

    return df
