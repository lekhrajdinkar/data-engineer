from pyspark.sql import SparkSession
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from src.databaseModule.db_connection_util import DATABASE_URL

# Function to create and configure the database connection
def get_db_session():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session(), engine

# Function to save DataFrame to the database using SQLAlchemy ORM
def save_dataframe_to_db(df, session, entity_class):
    try:
        # Iterate through PySpark DataFrame rows
        records = []
        for row in df.collect():  # Convert DataFrame rows to Python objects
            record = entity_class(
                id=row['id'],
                fund=row['fund'],
                price=row['price'],
                quantity=row['quantity']
            )
            records.append(record)

        # Perform the transaction
        session.add_all(records)
        session.commit()
        print(f"Successfully saved {len(records)} records to the database.")

    except SQLAlchemyError as e:
        session.rollback()
        print(f"An error occurred: {str(e)}")
    finally:
        session.close()
