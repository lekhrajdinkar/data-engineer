## 1. Converting RDD to DataFrame
```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import SparkSession

sc = SparkSession.builder.appName("MyApp").getOrCreate()
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
rdd = sc.parallelize(data)

schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

df = sc.createDataFrame(rdd, schema)
df.show() # print
df.explain() # prints the execution plan
```

## 2. transformation
```python

```