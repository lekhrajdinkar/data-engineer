```
📜 Historical Timeline & Key Technologies
1. Pre-Big Data Era (Before 2003)
   Relational Databases (e.g., Oracle, MySQL, SQL Server)
   Worked well for structured data & single-machine workloads


2. Google Influence (2003–2006)
   Google published 3 groundbreaking papers:
        Google File System (GFS) – distributed file storage
        MapReduce – programming model for parallel processing
        Bigtable – scalable, distributed database
```

3. Apache Takes Over (2006–2012)

| Year | Tech                          | Category                   | Description                                   |
| ---- | ----------------------------- | -------------------------- | --------------------------------------------- |
| 2006 | **Hadoop** (HDFS + MapReduce) | Storage + Batch Processing | Open-source version of GFS + MapReduce        |
| 2007 | **Hive**                      | SQL on Hadoop              | SQL-like queries on HDFS using MapReduce      |
| 2008 | **HBase**                     | NoSQL DB                   | Open-source Bigtable alternative              |
| 2009 | **Pig**                       | Data Flow Language         | Scripting for data transformation on Hadoop   |
| 2011 | **ZooKeeper**                 | Coordination               | Distributed system coordination               |
| 2012 | **Sqoop** / **Flume**         | Data Ingestion             | Sqoop for SQL ↔ Hadoop, Flume for logs/events |


4.   The Real-time Shift (2013–2017)

| Year | Tech                     | Category           | Description                                                  |
| ---- |--------------------------| ------------------ | ------------------------------------------------------------ |
| 2013 | **YARN**                 | Resource Manager   | Decoupled resource manager from Hadoop                       |
| 2014 | **Spark**  🔸  ✔️           | In-Memory Compute  | Faster than MapReduce, real-time + batch                     |
| 2014 | **Kafka**  🔸  ✔️        | Streaming Platform | Distributed log + pub-sub for real-time                      |
| 2015 | **Flink**  🔸  ✔️           | Stream Processing  | True real-time dataflow engine                               |
| 2015 | **Storm**                | Stream Processing  | Real-time analytics at scale (Twitter’s tech)                |
| 2016 | **Presto (by Facebook)** | Query Engine       | Fast SQL queries across data lakes                           |
| 2016 | **Parquet / ORC**  🔸    | Storage Format     | Columnar formats for big data (high compression, fast scans) |

5. Modern Big Data Ecosystem (2018–present)

| Tech                                           | Category                    | Description                          |
|------------------------------------------------|-----------------------------|--------------------------------------|
| **Delta Lake** / **Apache Iceberg** / **Hudi** | Lakehouse / Data Versioning | ACID on data lakes                   |
| **Snowflake**, **Databricks**, **BigQuery**    | Cloud Data Warehousing      | Merges warehouse + lake              |
| **Airflow**, **Dagster**                       | Orchestration               | DAG-based data pipelines             |
| **dbt (data build tool)**                      | Data Modeling               | SQL-based transformation             |
| **ClickHouse**, **Druid**                      | OLAP Engines                | Fast analytics on large data         |
| **MLflow**, **SageMaker**, **Spark MLlib**     | ML on Big Data              | Model tracking & distributed ML      |
| **OpenSearch**, **Elasticsearch**              | Search Analytics            | Distributed full-text + log analysis |
| redshift                                       | Analytics                   | complex SQL based analytics          |

---

##  Why Was Big Data So Popular?
```
Explosion of data from web, IoT, social media

Limitations of traditional RDBMS

Need for distributed computing

Demand for faster insights & real-time analytics

Rise of cloud & cheap storage
```
