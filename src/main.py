import sys
from pyspark.sql import SparkSession
from src.etlModule.filter.filter_1 import filter_demo
from src.etlModule.transformer.controller import apply_transformations
from src.commonModule.init_srv import load_env_config, load_etl_config
from src.databaseModule.entity.FundEntity import FundEntity
from src.databaseModule.save_dataframe_2_db import save_dataframe_to_db, get_db_session, save_dataframe_to_db_generic

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

etlapp = FastAPI()
sparkGlobalSession = SparkSession.builder.appName("PySpark-ETL-session").getOrCreate()

@etlapp.get("/")
async def read_root():
    return {"message": "ETL API is running"}

class ETLRequest(BaseModel):
    etl_name: str

@etlapp.post("/run_etl/")
async def run_etl_api(etl_request: ETLRequest):
    try:
        result = main(etl_request.etl_name)
        if result['status'] == 'error':
            raise HTTPException(status_code=500, detail=result['message'])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def main(etl_name):
    try:
        #etl_name = sys.argv[1]
        print(f"Running ETL job for: {etl_name}")
        app_config=load_env_config()
        etl_config: dict = load_etl_config(etl_name)
        print(etl_config)
        input_path = etl_config['input_path']
        output_path = etl_config['output_path']
        sparkGlobalSession = SparkSession.builder.appName("PySpark-ETL-session-"+etl_name).getOrCreate()

        df = sparkGlobalSession.read.option("header", "true").csv(input_path)  # Use the header option

        df_transformed = apply_transformations(df, etl_config['transformations'])
        df_filtered = filter_demo(df_transformed, etl_config['filters']['f0-demo'])

        df_filtered.write.csv(output_path, mode='overwrite', header=True)
        print(f"Data successfully stored in the csv file")

        if etl_config['output_to_db'] == True :
            session, engine = get_db_session()
            FundEntity.metadata.create_all(engine) # create table
            #save_dataframe_to_db_generic(df, session, FundEntity)
            save_dataframe_to_db(df, session, FundEntity)

        # spark.stop()
        return {
            "status": "success",
            "message": f"ETL - {etl_name} process completed successfully"
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    etl_name = sys.argv[1] # reading command line arg
    main(etl_name)
