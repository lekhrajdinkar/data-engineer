from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("Parquet and ORC Inspection") \
    .getOrCreate()

# Sample data
data = [
    (1, "Alice", 1000.0),
    (2, "Bob", 1500.0),
    (3, "Charlie", 2000.0)
]
columns = ["id", "name", "salary"]

# Create a DataFrame
df = spark.createDataFrame(data, schema=columns)

# Write DataFrame to Parquet and ORC formats
parquet_path = "output/sample.parquet"
orc_path = "output/sample.orc"

df.write.mode("overwrite").parquet(parquet_path)
df.write.mode("overwrite").orc(orc_path)

# Read and display the Parquet file schema and data
print("=== Parquet File ===")
parquet_df = spark.read.parquet(parquet_path)
parquet_df.printSchema()
parquet_df.show(truncate=False)

# Read and display the ORC file schema and data
print("\n=== ORC File ===")
orc_df = spark.read.orc(orc_path)
orc_df.printSchema()
orc_df.show(truncate=False)

# Stop Spark Session
spark.stop()
