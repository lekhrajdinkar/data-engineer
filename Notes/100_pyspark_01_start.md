# interview topic
## Create 
- rdd = sc.parallelize(data)
- spark.createDataFrame(rdd, schema)
  
## 1 basic
- df.**select**("col-1") - chooses existing columns

## 2 transformation 
- lazy operations that create a new RDD
- don't execute until an action is called
- Each transformation returns a new DataFrame
- chain transformations for better readability
```python
df.filter(df.age > 30).show()
df.where(df.age > 30).show()

df.withColumn("age_plus_10", col("age") + 10).show() - adds/modifies a column

df.withColumnRenamed("age", "years").show()

df.na.drop().show()                       # drop rows with any null
df.na.drop(subset=["age"]).show()         # drop rows with null in age

df.na.fill(0).show()                      # fill all nulls with 0
df.na.fill({"age": 0, "name": "Unknown"}).show()  # column-specific

df.groupBy("year").pivot("quarter").sum("revenue").show()

df.withColumn("item", explode("items_array")).show() # Expand arrays/maps

# === Chain ===
(df.filter(df.age > 25)
 .groupBy("department")
 .agg(avg("salary").alias("avg_salary"))
 .orderBy("avg_salary", ascending=False)
 .show())
```

## 3 action: groupBy, agg, join
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



## 4 performance : optimize a slow PySpark job
- **df.dropDuplicates()**
- **repartition() and coalesce()**
  - repartition() shuffles data to increase/decrease partitions.
  - coalesce() reduces partitions without a full shuffle.
  - avoid shuffles. **
- **broadcast variable** 
  - a read-only variable cached on each worker to avoid shipping it multiple times (used for small lookup tables).
  - using broadcast joins
- **Partitioning**
- **caching** 
  - cache() : storing RDD/DataFrame MEMORY_ONLY
  - persist() : allows different storage levels (e.g., MEMORY, DISK)
- **tuning executor memory**

## scenarios
- **handle missing values**
  - df.na.fill() or df.na.drop()
- **Spark SQL**
  - df.createOrReplaceTempView("table")
  - spark.sql("SELECT * FROM table")

