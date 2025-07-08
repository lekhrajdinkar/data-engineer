from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, regexp_replace, when, lit
from pyspark.sql.types import StringType, DateType
import logging
from datetime import datetime

class UserETL:
    def __init__(self, db_url):
        self.spark = SparkSession.builder \
            .appName("UserETL") \
            .config("spark.jars.packages", "org.postgresql:postgresql:42.2.18") \
            .getOrCreate()

        self.db_url = db_url
        self.db_properties = {
            "user": "your_username",
            "password": "your_password",
            "driver": "org.postgresql.Driver"-
        }

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("UserETL")

    def load_csv(self, file_path):
        """Load CSV file into Spark DataFrame"""
        try:
            df = self.spark.read.csv(
                file_path,
                header=True,
                inferSchema=True,
                nullValue="NA"
            )
            self.logger.info(f"Successfully loaded CSV file with {df.count()} records")
            return df
        except Exception as e:
            self.logger.error(f"Error loading CSV file: {str(e)}")
            raise

    def transform_data(self, df):
        """Perform data transformations and cleaning"""
        try:
            # Clean email addresses
            df = df.withColumn("email",
                               when(col("email").rlike("^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$"),
                                    col("email"))
                               .otherwise(lit(None)))

            # Standardize names
            df = df.withColumn("first_name", upper(col("first_name")))
            df = df.withColumn("last_name", upper(col("last_name")))

            # Clean phone numbers
            df = df.withColumn("phone",
                               regexp_replace(col("phone"), "[^0-9]", ""))

            # Convert date strings to date type
            df = df.withColumn("birth_date",
                               when(col("birth_date").rlike("^\\d{4}-\\d{2}-\\d{2}$"),
                                    col("birth_date"))
                               .otherwise(lit(None)))

            # Add audit columns
            current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            df = df.withColumn("etl_load_date", lit(current_timestamp))

            self.logger.info("Data transformations completed successfully")
            return df
        except Exception as e:
            self.logger.error(f"Error during data transformation: {str(e)}")
            raise

    def load_to_stage(self, df, batch_size=50000):
        """Load transformed data to staging table in batches"""
        try:
            # Write to stage table in batches
            (df.write
             .option("batchsize", batch_size)
             .jdbc(url=self.db_url,
                   table="user_stage",
                   mode="overwrite",
                   properties=self.db_properties))

            self.logger.info(f"Successfully loaded {df.count()} records to stage table")
        except Exception as e:
            self.logger.error(f"Error loading to stage table: {str(e)}")
            raise

    def load_to_target(self):
        """Load data from stage to target user table"""
        try:
            # Read from stage table
            stage_df = self.spark.read.jdbc(
                url=self.db_url,
                table="(SELECT * FROM user_stage) as stage_data",
                properties=self.db_properties
            )

            # Perform any additional transformations if needed
            final_df = stage_df.drop("etl_load_date")

            # Write to target table
            (final_df.write
             .jdbc(url=self.db_url,
                   table="user",
                   mode="append",
                   properties=self.db_properties))

            self.logger.info(f"Successfully loaded {final_df.count()} records to target table")
            return True
        except Exception as e:
            self.logger.error(f"Error loading to target table: {str(e)}")
            raise

    def run_etl(self, csv_path):
        """Execute full ETL pipeline"""
        try:
            # Extract
            raw_df = self.load_csv(csv_path)

            # Transform
            transformed_df = self.transform_data(raw_df)

            # Load to stage
            self.load_to_stage(transformed_df)

            # Load to target
            self.load_to_target()

            self.logger.info("ETL process completed successfully")
            return True
        except Exception as e:
            self.logger.error(f"ETL process failed: {str(e)}")
            return False