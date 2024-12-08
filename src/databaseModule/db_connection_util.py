from commonModule.init_srv import load_env_config
from sqlalchemy import create_engine

app_config = load_env_config();
db_config = app_config['db']

db_host = db_config['host']
db_port = db_config['port']
db_user = db_config['user']
db_password = db_config['password']
db_name = db_config['database']

DATABASE_URL = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

def test_connection() :
    engine = create_engine(DATABASE_URL,echo=True)
    try:
        with engine.connect() as connection:
            print(f"Connected to the database {DATABASE_URL} successfully!")
    except Exception as e:
        print(f"Failed to connect to the database: {e}")

