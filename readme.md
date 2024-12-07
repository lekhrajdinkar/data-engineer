# reference:
- https://chatgpt.com/c/6754cff4-b63c-800d-9e2f-caba7735697e
---

# project Structure
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
