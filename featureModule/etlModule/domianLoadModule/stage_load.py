from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.master("local[*]").appName("ETLJob").getOrCreate()

# Read CSV
df = spark.read.csv("s3://bucket/input.csv", header=True, inferSchema=True)

# Transform data (example: filter and add column)
df_transformed = df.filter(df["status"] == "active").withColumn("processed_date", current_date())

# Write to database
df_transformed.write.jdbc(
    url="jdbc:postgresql://db-host:5432/mydb",
    table="etl_table",
    mode="append",
    properties={"user": "username", "password": "password", "batchsize": "1000"}
)

# Stop Spark session
spark.stop()
