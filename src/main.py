import json
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def load_config(etl_name: str):
    # Load configuration for the given etl_name
    try:
        with open(f'config/{etl_name}-config.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Configuration file for {etl_name} not found.")
        sys.exit(1)

def transform_data(df, config):
    # Apply transformation based on the config
    transformation = config.get('transformation')

    if transformation == 'multiply_by_2':
        df = df.withColumn(config['derived_column_name'], col('existing_column') * 2)
    elif transformation == 'add_10':
        df = df.withColumn(config['derived_column_name'], col('existing_column') + 10)

    # Remove specified columns
    columns_to_remove = config['columns_to_remove']
    for column in columns_to_remove:
        df = df.drop(column)

    return df

def main():
    # Get etl-name from the command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <etl-name>")
        sys.exit(1)

    etl_name = sys.argv[1]
    print(f"Running ETL job for: {etl_name}")

    # Load the configuration for the given ETL
    config = load_config(etl_name)

    # Initialize Spark session
    spark = SparkSession.builder.appName("PySparkETL").getOrCreate()

    # Read input data from the specified source
    input_path = config['input_path']
    df = spark.read.option("header", "true").csv(input_path)  # Use the header option

    # Transform the data according to the config
    df_transformed = transform_data(df, config)

    # Write the output data to the target directory
    output_path = config['output_path']
    df_transformed.write.csv(output_path, mode='overwrite', header=True)

    spark.stop()


if __name__ == "__main__":
    main()
