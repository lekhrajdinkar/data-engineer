# interview topic
## 0 Create 
- data = [1,2,3,4,5]
- rdd = spark.parallelize(data)
- spark.createDataFrame(rdd, schema)
  
## 1 select / delete
- df.**select**("col-1") - chooses existing columns

## 2 transformation / update 
- lazy operations that create a new RDD / df
  - don't execute until an action is called
- Each transformation returns a new DataFrame
- chain transformations for better readability
- map()
  - Applies a function/lambda to each **row** of the DataFrame
  - Row-wise transformations,  One row at a time.
- mapPartition(): Applies a function/lambda to each **partition** (instead of each row)
```python
def lambda1(iterator):
  for row in iterator:
    yield (row.number * 10,)
df.rdd.map(lambda x: x * 2)
df.rdd.map(lambda1)

df.filter(df.age > 30).show()
df.where(df.age > 30).show()

df.withColumn("age_plus_10", col("age") + 10).show() # adds/modifies a column

df.withColumnRenamed("age", "years").show()

# ==== handle NULL  ===
df.na.drop().show()                       # drop rows with any null
df.na.drop(subset=["age"]).show()         # drop rows with null in age

df.na.fill(0).show()                      # fill all nulls with 0
df.na.fill({"age": 0, "name": "Unknown"}).show()  # column-specific

# ==== handle duplicate  ===
df.dropDuplicates() # expensive
df.dropDuplicates(subset=['key_column'])  # Specify only necessary columns

# ==== Pivot ===
df.groupBy("year").pivot("quarter").sum("revenue").show()
df.groupBy("year") .pivot("quarter").agg(sum("revenue").alias("revenue"),sum("profit").alias("profit")).show()
'''
+----+-------+-------+-------+
|year|quarter|revenue|profit |
+----+-------+-------+-------+
|2023|      1|    100|     20|
|2023|      2|    150|     30|
|2023|      3|    200|     40|
|2023|      4|    120|     25|
+----+-------+-------+-------+  

+----+---+---+---+---+
|year|  1|  2|  3|  4|
+----+---+---+---+---+
|2023|100|150|200|120|
+----+---+---+---+---+

+----+---------+---------+---------+---------+--------+--------+--------+--------+
|year|1_revenue|1_profit |2_revenue|2_profit |3_revenue|3_profit|4_revenue|4_profit|
+----+---------+---------+---------+---------+---------+--------+---------+--------+
|2023|      100|       20|      150|       30|      200|      40|      120|      25|
|2024|      180|       35|       90|       15|      210|      45|      130|      30|
+----+---------+---------+---------+---------+---------+--------+---------+--------+
'''

df.withColumn("item", explode("items_array")).show() # Expand arrays/maps

# === Chain ===

(df.filter(df.age > 25)
 .groupBy("department")
 .agg(avg("salary").alias("avg_salary"))
 .orderBy("avg_salary", ascending=False)
 .show())
```

## 3 action: groupBy, agg, join, order
- agg === having in sql
```python
df.groupBy("department").count().show()

df.groupBy("department").agg(
  avg("salary").alias("avg_salary"),
  max("age").alias("max_age")
  ).show()

employees.join(departments,
               employees.dept_id == departments.id,
               "inner").show()

df.orderBy("age").show()                  # ascending

df.orderBy(df.age.desc()).show()          # descending

df.orderBy(["age", "name"], ascending=[0, 1]).show()  # mixed
```

---
## 98 performance : optimize a slow PySpark job
### cache
```python
# CACHE :: Data reused multiple times + Small enough to fit in cluster memory
from pyspark.storagelevel import StorageLevel
df.persist(StorageLevel.MEMORY_AND_DISK)

df.cache()  # or df.persist(StorageLevel.MEMORY_ONLY)
df.unpersist() # # Don't forget to unpersist!
```
### df.dropDuplicates()

### Partitioning
- repartition(200, "department_id") : shuffles data to increase/decrease partitions.
- coalesce(50) : reduces partitions without a full shuffle.

### avoid shuffles.
```python
# Bad - causes shuffle
df.orderBy("timestamp")
# Better - use partitioning
df.repartition("date_column").sortWithinPartitions("timestamp")

# Worst - multiple shuffles
df.groupBy("a").agg(...).groupBy("b").agg(...)
# Better - single aggregation
df.groupBy("a", "b").agg(...)
```

### broadcast variable and join :point_left:
- a read-only variable cached on each worker to avoid shipping it multiple times 
- used for small lookup table.
```python
from pyspark import SparkContext
sc = SparkContext()
# Small lookup dictionary
country_codes = {    "US": "United States",    "IN": "India",    "UK": "United Kingdom"}

broadcast_codes = sc.broadcast(country_codes) # Create broadcast variable

# Use in RDD operations
rdd = sc.parallelize(["US", "IN", "UK", "IN", "US"])
full_names = rdd.map(lambda x: broadcast_codes.value[x])
full_names.collect()
# Returns: ['United States', 'India', 'United Kingdom', 'India', 'United States']
```
- **Broadcast join**
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast

spark = SparkSession.builder.getOrCreate()

# Large fact table
transactions = spark.createDataFrame([
  (1, "US", 100), (2, "IN", 200), (3, "UK", 300),
  (4, "US", 150), (5, "IN", 250)], ["id", "country", "amount"])

# Small dimension table
countries = spark.createDataFrame([
  ("US", "United States"), ("IN", "India"),
  ("UK", "United Kingdom")], ["code", "name"])

# Standard join (shuffle join)
transactions.join(countries, transactions.country == countries.code).show()

# Broadcast join (more efficient)
transactions.join(broadcast(countries), transactions.country == countries.code).show()
```

### tuning executor memory
```
spark-submit \
  --executor-memory 8G \
  --executor-cores 4 \
  --num-executors 10 \
  --conf spark.memory.fraction=0.8 \
  --conf spark.memory.storageFraction=0.3 \
  your_app.py
```
### File Format Optimization
- df.write.**parquet**("output.parquet")
- df.write.**format**("avro").save("output.avro")
- df.**repartition(100)**.write.parquet("output")  # 100 files -  **Control file size**
---
## 99 scenarios
- **handle missing values**
  - df.na.fill() or df.na.drop()
- **Spark SQL**
  - df.createOrReplaceTempView("table")
  - spark.sql("SELECT * FROM table")

