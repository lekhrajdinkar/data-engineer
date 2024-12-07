from pyspark.sql import DataFrame

def validate_data(df: DataFrame) -> DataFrame:
    """
    Basic validation to ensure no null values in critical columns.
    """
    if df.filter(df['id'].isNull()).count() > 0:
        raise ValueError("Validation failed: 'id' column contains null values.")
    return df
