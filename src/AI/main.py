from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from etl_job import UserETL
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import logging
from typing import Optional

# Database configuration
DATABASE_URL = "postgresql://username:password@localhost:5432/your_database"

# FastAPI app
app = FastAPI(title="User ETL Service")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FastAPI")

# Database engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_db():
    """Database session context manager"""
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(status_code=500, detail="Database operation failed")
    finally:
        db.close()

class ETLRequest(BaseModel):
    csv_path: str
    batch_size: Optional[int] = 50000

@app.post("/run-etl")
async def run_etl(etl_request: ETLRequest):
    """Endpoint to trigger ETL process"""
    try:
        # Initialize ETL processor
        etl_processor = UserETL(DATABASE_URL)

        # Run ETL
        success = etl_processor.run_etl(etl_request.csv_path)

        if success:
            return {"status": "success", "message": "ETL completed successfully"}
        else:
            raise HTTPException(status_code=500, detail="ETL process failed")

    except Exception as e:
        logger.error(f"ETL process error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/etl-status")
async def get_etl_status():
    """Check ETL status from database"""
    try:
        with get_db() as db:
            # Check records in stage table
            stage_count = db.execute(text("SELECT COUNT(*) FROM user_stage")).scalar()

            # Check records in target table
            target_count = db.execute(text("SELECT COUNT(*) FROM user")).scalar()

            return {
                "stage_record_count": stage_count,
                "target_record_count": target_count,
                "status": "available"
            }
    except Exception as e:
        logger.error(f"Status check error: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to check ETL status")

@app.post("/clean-tables")
async def clean_tables():
    """Clean both stage and target tables"""
    try:
        with get_db() as db:
            db.execute(text("TRUNCATE TABLE user_stage"))
            db.execute(text("TRUNCATE TABLE user"))
            return {"status": "success", "message": "Tables cleaned successfully"}
    except Exception as e:
        logger.error(f"Clean tables error: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to clean tables")