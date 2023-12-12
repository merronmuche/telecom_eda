
from sqlalchemy import create_engine


print(__name__)

def connect_to_postgres():

    database_name = 'telecom'
    table_name= 'xdr_data'

    connection_params = { "host": "localhost", "user": "postgres", "password": "postgres",
                        "port": "5432", "database": database_name}

    engine = create_engine(f"postgresql+psycopg2://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/{connection_params['database']}")

    return engine


if __name__ == "__main__":
    connect_to_postgres()