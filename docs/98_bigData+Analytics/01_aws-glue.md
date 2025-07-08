## intro
- fully managed serverless
- **data integration service**
- Building **serverless data pipelines** ⬅️
- Discover, prepare, clean, transform, and move data between data stores
- supports **structured and semi-structured** data like CSV, JSON, Parquet, Avro,
- build **ETL** (Extract, Transform, Load) or ELT pipelines for:
    - batch processing 
        - S3 to Redshift 
        - S3 to Snowflake 
    - streaming data. (from kafka)

## Component
| Component                                      | Description                                                                                                                                                      |
| ---------------------------------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Glue Crawler**                               | Scans your data sources (S3, JDBC, etc.), detects schema, and creates metadata tables in **AWS Glue Data Catalog**. Think of this as automated schema inference. |
| **Data Catalog**                               | Central metadata repository. It stores metadata like table names, schema, data format, partition info, etc. Used by Glue Jobs, Athena, Redshift Spectrum, etc.   |
| **Glue Jobs**                                  | The core ETL process. Written in **PySpark or Scala**. It reads from source, transforms data, and writes to target (S3, RDS, Redshift, etc.).                    |
| **Glue Studio**                                | Visual UI to build and run ETL pipelines (drag & drop, no code/low code).                                                                                        |
| **Glue DataBrew**                              | GUI-based tool for data preparation (cleaning, normalization, enrichment). Great for non-coders or quick transformations.                                        |
| **Glue Streaming Jobs**                        | For processing streaming data (Kinesis, Kafka). Used for near real-time ETL.                                                                                     |
| **Job Bookmarking**                            | Prevents reprocessing of already-processed data by keeping track of what has been processed. Useful in incremental loads.                                        |
| **Elastic Views** *(Deprecated/Being Retired)* | Previously allowed combining data across stores using materialized views; AWS is discontinuing it in 2024.                                                       |
| **Glue Connectors**                            | Ready-made connectors to read/write from JDBC, Snowflake, MongoDB, Kafka, etc.                                                                                   |
| **Glue Triggers & Workflows**                  | Orchestration and automation of multiple jobs with conditions and dependencies.                                                                                  |


