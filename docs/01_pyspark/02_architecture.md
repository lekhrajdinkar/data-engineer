## Intro
- open-source
- in memory processing
- **distributed** computing system used for big data processing.
- **Fault-tolerant**
- **Highly scalable** (thousands of nodes)
- fast (100x faster than Hadoop MapReduce in memory)
- unified engine for:
  - ELL/batch processing
  - stream processing
  - SQL
  - machine learning
  - graph processing


## deployment model 
- cluster setup can be done with :
    - **Databricks** (managed Spark) 
    - **Local** (for development)
    - **YARN** (Hadoop)
    - **Kubernetes**
    - **Standalone cluster**: Spark’s own cluster manager (Local mode)
      - this is what used in local project
      - ggcc etl project

---

## core-Component
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

## RDD
- Resilient Distributed Dataset
- immutable
- partitioned collections of data

## dataframes / df
- Higher-level abstractions built on top of `RDD`
- `Structured` data with a schema
- **dataset** - typed version of df.
- **Spark-SQL** 
  - module for processing structured data using SQL-like queries.
  - like joins, aggregations, and filtering

## cluster-manager node
### driver program
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

## worker node/s
### Job / Execution Model (DAG)
- PySpark creates a DAG (Directed Acyclic Graph) of stages and tasks.
- Stages break into tasks, which are distributed to executors.

```
DAG : 
Is deterministic and order-controlled

 A → B → C
      ↓
      D
      
- job-1 
  - stage-1 (task-1)
    - task-1.1 ( on partition-1)
    - task-1.2 ( on partition-2)
    - ...
    
==========

PySpark App
   |
Driver Program (your script)
   |
SparkSession (entry point)
   |
Cluster Manager (e.g., YARN, Mesos, Kubernetes, Standalone)
   |
Executors (run tasks on worker nodes)

=============

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

### Task
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

### Executors 
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
   