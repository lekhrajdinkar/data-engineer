# A. Spark::`Intro`
- `polyglot` (Scala, Python [PySpark], Java, R, and SQL) + CLI
- wide libraries for a variety of tasks.
- 100 times faster than **MapReduce** for processing large amounts of data.
- `open-source` engine for data processing on computer clusters

- Designed for processing **large-scale datasets** on `distributed machines` (parallel)
  - unstructured, semi-structured, and structured data
  - Powerful Caching
  - in-memory processing / real-time computation

## **use case**:
- for big data analytics,
- machine learning on large datasets.
- ETL (Extract, Transform, Load) pipelines

## `deployment model` for distributed architecture:
- cluster setup can be done with :
  - **Mesos**
  - **YARN** (Hadoop)
  - **Kubernetes**
  - **Standalone**: Spark’s own cluster manager
    - this is what used in local project
    - ccgg etl project

## fault tolerance
- Automatic recovery mechanisms 
  - If a partition is lost, Spark can recompute it using the **lineage graph**

---

# B. Spark::`core-Component`
```
+---------------------+      +-------------------------+
|  Driver Program     | ---> |   Cluster Manager       |
+---------------------+      +-------------------------+
           |
           V
+---------------------+      +-------------------------+
|   Worker Node 1     | ---> |   Executor 1 (Tasks)    |
+---------------------+      +-------------------------+
           |
           V
+---------------------+      +-------------------------+
|   Worker Node 2     | ---> |   Executor 2 (Tasks)    |
+---------------------+      +-------------------------+

```
## 1. RDD
- Resilient Distributed Dataset
- immutable
- partitioned collections of data

### 1.1 dataframes / df
- Higher-level abstractions built on top of `RDD`
- `Structured` data with a schema
- **dataset** - typed version of df.
- **Spark-SQL** 
  - module for processing structured data using SQL-like queries.
  - like joins, aggregations, and filtering

## 2. cluster-manager node
### 2.1. driver program
- runs cluster-manager node
- entry point of the PySpark-app-1
- duties:
  - Initiates `SparkContext`
    - Acts as the gateway to the Spark cluster for PySpark-app-1
    - object to manage lifecycle of PySpark-app-1
  - Creates `RDDs/DataFrames` 
    - Defines the transformations 
    - actions for data processing. 
  - `Schedules Tasks`
    - Breaks the job into stages and task for execution on worker nodes. 
  - `Collects Results` 
    - Aggregates results from executors and returns them to the client.

- resource management across the cluster
  - assigns resources (CPU, memory) to the `driver` and `executor nodes`

## 3. worker node/s
### 3.1. Task
- Tasks are `units of work` created by dividing the data into partitions.
- Tasks run in parallel across `executors`.
- operations:
  - **transformations**
    - map, 
    - filter
    - ...
  - **actions**
    - count
    - collect
    - ...

### 3.2. Executors (parallelism)
- `distributed processes` that run on **worker nodes**.
- Executes the `tasks` assigned by the driver (on **partitions of the data**)
- caching/persistence
  - Storing data in memory or disk for **intermediate computation**
- Reporting **task status**
- send **results** back to the driver


---  
# C. Spark::`Ecosystem`
## Core API
## Spark SQL
## Spark streaming
## Spark Mlib
## spark GraphX
   