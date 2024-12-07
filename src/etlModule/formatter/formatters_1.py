from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def format_data(df: DataFrame) -> DataFrame:
    """
    Format the data: e.g., trimming whitespace from string columns.
    """
    return df.select([col(c).alias(c.strip()) if isinstance(c, str) else c for c in df.columns])
