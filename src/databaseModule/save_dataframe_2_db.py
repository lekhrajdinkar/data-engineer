from pyspark.sql import SparkSession, DataFrame
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
from src.databaseModule.db_connection_util import DATABASE_URL
from typing import Type

from src.databaseModule.entity.Base import Base
from src.databaseModule.entity.FundEntity import FundEntity


# Function to create and configure the database connection
def get_db_session():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session(), engine

# Function to save DataFrame to the database using SQLAlchemy ORM
def save_dataframe_to_db(df: DataFrame, session: Session, entity_class: Type[FundEntity]):
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


def save_dataframe_to_db_generic(session: Session, df: DataFrame, entity_class: Type[Base]):
    records = df.collect()  # Get all rows from PySpark DataFrame as a list of Row objects
    data_dicts = [row.asDict() for row in records]  # Convert each Row to a dictionary

    # Create instances of the entity class
    entities = [entity_class(**data) for data in data_dicts]

    # Add to session and commit the transaction
    session.add_all(entities)
    session.commit()

    print(f"Successfully saved {len(entities)} records to the database.")

def save_dataframe_to_db_generic2(session: Session, df: DataFrame, entity_class: Type[Base]):
    records = df.collect()  # Correct: collect() should be applied on df, which is a PySpark DataFrame
    data_dicts = [row.asDict() for row in records]
    entities = [entity_class(**data) for data in data_dicts]
    session.add_all(entities)  # Add to session
    session.commit()  # Commit the transaction
    print(f"Successfully saved {len(entities)} records to the database.")
