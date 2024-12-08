from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SaveToDatabase").getOrCreate()

data = [
    (1, "fund_1", 5.0, 5),
    (2, "fund_2", 10.0, 6),
    (3, "fund_3", 7.5, 7),
    (4, "fund_4", 3.0, 8)
]
columns = ["id", "fund", "price", "quantity"]
df = spark.createDataFrame(data, schema=columns)