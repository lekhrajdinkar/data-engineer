## references
- <a href="https://chatgpt.com/c/6756481b-c08c-800d-9b78-2e024a506c16" target="_blank">parquet and orc format</a>

--- 
# A. Spark::Intro
- `polyglot` (Scala, Python [PySpark], Java, R, and SQL) + CLI
- wide libraries for a variety of tasks.
- 100 times faster than **MapReduce** for processing large amounts of data.
- `open-source` engine for data processing on computer clusters

- Designed for processing **large-scale datasets** on `distributed machines` (parallel)
  - unstructured, semi-structured, and structured data
  - Powerful Caching
  - in-memory processing / real-time computation

## use case:
- for big data analytics,
- machine learning on large datasets.
- ETL (Extract, Transform, Load) pipelines

## `deployment model` for distributed architecture:
- cluster setup can be done with :
  - **Mesos**
  - **YARN** (Hadoop)
  - **Kubernetes**
  - **Standalone**: Spark’s own cluster manager (Local mode)
    - this is what used in local project
    - ggcc etl project

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
### 3.1. Job / DAG
- highest-level unit of work in Spark.
- think f --> entire **execution path** from the input-data to the final-result
- When an action is invoked on df, Spark computes the full **Directed Acyclic Graph** (`DAG`)
- DAG is divided into **stages**, based on transformations.
- **stages are distributed to worker nodes as tasks**. ⬅️
- job-1 
  - stage-1 (task-1)
    - task-1.1 ( on partition-1)
    - task-1.2 ( on partition-2)
    - ...
```
# 1. This action triggers a Spark job

df = spark.read.csv("data.csv")
df = df.filter(df["age"] > 30)
df = df.groupBy("city").count()
df.show()

# 2. DAG
[Input Data] --> [Filter] --> [Shuffle] --> [GroupBy] --> [Count]

# 3. split in task/stages
Stage 1: Input Data --> Filter
Stage 2: Shuffle --> GroupBy --> Count

```
### 3.2. Task
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

### 3.2. Executors 
- task executor.
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
   