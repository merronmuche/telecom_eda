

import pandas as pd
from postgres_connection import connect_to_postgres


def get_df():
    engine = connect_to_postgres()

    sql_query = 'SELECT * FROM xdr_data'
    df = pd.read_sql(sql_query, con=engine)

    return df

if __name__ == "__main__":

    df = get_df()
    