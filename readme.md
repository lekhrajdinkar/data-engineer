[Notes](Notes)
---
# project Structure
- database : [docker-compose-postgres.yml](docker-compose-postgres.yml)
- lsof -i :8000
-  fastapi : http://127.0.0.1:8000/run_etl
  - swagger : http://localhost:8000/docs
```
body:
{
    "etl_name" : "etl-1"
}

response:
{
    "status": "success",
    "message": "ETL - etl-1 process completed successfully"
}
```
```
# /Users/lekhrajdinkar/Documents/GitHub/02-etl-pyspark

02-etl-pyspark/
│
├── Notes
├── DIR_SOURCE
│   ├── etl-1-source.csv
│   ├── etl-2-source.csv
│   ├── ...
├── DIR_TARGET
├── config/
│   ├── etl-1.json
│   └── etl-2.json
│   └── ...
├── src/
│   ├── module1
│   ├── module2
│   ├── ...
│   ├── etlModule
│   │   ├── validator.py
│   │   ├── formatter.py
│   │   ├── transformer.py
│   │   └── __init__.py
│   ├── main.py
└── requirements.txt
└── Dockerfile
└── app_run.sh

```
- Notes: A directory likely containing documentation or project notes.
- DIR_SOURCE: The source data directory containing CSV files for ETL processing.
- DIR_TARGET: Target directory where transformed data will be stored (not listed with specific files, but inferred from the structure).
- config: Contains configuration files (likely JSON), such as etl-1.json, which could define processing rules or mappings for different ETL steps.
- **src**: The main source code directory.
  - module1
  - module2, 
  - ...
  - Different functional modules or libraries.
  - **etlModule**: The core ETL logic, including:
    - **validator**: Handles data validation.
    - **formatter**: Manages data formatting.
    - **transformer**: Contains transformation logic for the ETL process.
  - `main.py`: The main entry point for running the ETL process.
- requirements.txt: Python dependencies needed for the project.
- Dockerfile: Used to containerize the application, likely for deployment or running in different environments.
- `app_run.sh`: A shell script to automate the execution of the application.

---
## Spark History Server
- Spark UI becomes unavailable after the Spark session stops because it is tied to the lifecycle of the session
- persist the Spark application event data and access it later for debugging or analysis.
- Configure Spark to log events to a director or s3:
```
# spark-defaults.conf

spark.eventLog.enabled true

spark.eventLog.dir hdfs://<path-to-hdfs> (or a local directory)

spark.eventLog.dir s3://your-bucket-name/spark-logs/
spark.hadoop.fs.s3a.access.key YOUR_ACCESS_KEY
spark.hadoop.fs.s3a.secret.key YOUR_SECRET_KEY
spark.hadoop.fs.s3a.impl org.apache.hadoop.fs.s3a.S3AFileSystem
```
- start: **./sbin/start-history-server.sh**
  - spark.history.fs.logDirectory <above-path>
  - http://<hostname>:18080