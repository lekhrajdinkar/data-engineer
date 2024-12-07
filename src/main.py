import json
import sys
from pyspark.sql import SparkSession

from etlModule.filter.filter_1 import filter_demo
from etlModule.transformer.transformer_1 import add_derived_col


def load_config(etl_name: str):
    # Load configuration for the given etl_name
    try:
        with open(f'config/{etl_name}-config.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Configuration file for {etl_name} not found.")
        sys.exit(1)

def main():
    etl_name = sys.argv[1]
    print(f"Running ETL job for: {etl_name}")
    etl_config = load_config(etl_name)
    input_path = etl_config['input_path']
    output_path = etl_config['output_path']
    spark = SparkSession.builder.appName("PySpark-ETL-session-"+etl_name).getOrCreate()

    df = spark.read.option("header", "true").csv(input_path)  # Use the header option

    df_transformed = add_derived_col(df, etl_config)
    df_filtered = filter_demo(df_transformed, etl_config)

    df_filtered.write.csv(output_path, mode='overwrite', header=True)

    spark.stop()

if __name__ == "__main__":
    main()
