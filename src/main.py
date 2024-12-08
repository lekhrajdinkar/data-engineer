import sys
from pyspark.sql import SparkSession
from etlModule.filter.filter_1 import filter_demo
from etlModule.transformer.controller import apply_transformations
from commonModule.init_srv import load_env_config, load_etl_config
from databaseModule.entity.FundEntity import FundEntity
from databaseModule.save_dataframe_2_db import save_dataframe_to_db, get_db_session


def main():
    etl_name = sys.argv[1]
    print(f"Running ETL job for: {etl_name}")
    app_config=load_env_config()
    etl_config: dict = load_etl_config(etl_name)
    input_path = etl_config['input_path']
    output_path = etl_config['output_path']
    spark = SparkSession.builder.appName("PySpark-ETL-session-"+etl_name).getOrCreate()

    df = spark.read.option("header", "true").csv(input_path)  # Use the header option

    df_transformed = apply_transformations(df, etl_config['transformations'])
    df_filtered = filter_demo(df_transformed, etl_config['filters']['f0-demo'])

    df_filtered.write.csv(output_path, mode='overwrite', header=True)
    print(f"Data successfully stored in the csv file")

    if etl_config['output_to_db'] == True :
        session, engine = get_db_session()
        FundEntity.metadata.create_all(engine) # create table
        save_dataframe_to_db(df, session, FundEntity)

    spark.stop()

if __name__ == "__main__":
    main()
