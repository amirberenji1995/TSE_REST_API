import sqlite3
import pandas as pd


def list_of_symbols():
    con = sqlite3.connect('/home/amir/venvs/new ones/finace_api/notebooks/tickers_data.db')
    cursorObj = con.cursor()

    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
    tables_list = cursorObj.fetchall()

    tables_list_str = []
    for item in tables_list:
        tables_list_str.append(''.join(item))

    return tables_list_str



def symbols_table(pk):
    con = sqlite3.connect('/home/amir/venvs/new ones/finace_api/notebooks/tickers_data.db')
    cur = con.cursor()
    df = pd.read_sql_query("SELECT * from {}".format(pk), con)
    return df


def df_filtering(df, start_date, end_date):
    after_start_date = df["date"] >= start_date
    before_end_date = df["date"] <= end_date
    between_two_dates = after_start_date & before_end_date
    df = df.loc[between_two_dates]
    return df
