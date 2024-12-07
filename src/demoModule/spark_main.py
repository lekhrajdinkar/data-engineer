from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.master("local[*]").appName("LocalSparkExample").getOrCreate()

# Example: Process a CSV
data = spark.read.csv("sample.csv", header=True, inferSchema=True)
data.show()

spark.stop()