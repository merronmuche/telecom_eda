from sqlalchemy import create_engine
import pandas as pd

def connect_to_postgres():
    database_name = 'telecom'
    table_name = 'xdr_data'

    connection_params = {"host": "localhost", "user": "postgres", "password": "postgres",
                         "port": "5434", "database": database_name}

    engine = create_engine(f"postgresql+psycopg2://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/{connection_params['database']}")

    return engine, table_name

def execute_sql_query(engine, table_name):
    # Example query to select all rows from the 'xdr_data' table
    query = f"SELECT * FROM {table_name};"
    
    # Execute the query and load the result into a DataFrame
    df = pd.read_sql_query(query, engine)

    # Display the DataFrame
    print(df)

if __name__ == "__main__":
    postgres_engine, table_name = connect_to_postgres()
    execute_sql_query(postgres_engine, table_name)
