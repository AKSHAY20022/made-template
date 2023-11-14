import requests
import pandas as pd
import sqlite3

DATA_URL = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"

# download and return the dataset as a DataFrame
def download_data(url):
    response = requests.get(url)
    with open('temp_data.csv', 'wb') as file:
        file.write(response.content)
    return pd.read_csv('temp_data.csv', on_bad_lines='skip')

# insert the data into the SQLite table
def insert_data(df, db_name):
    with sqlite3.connect(db_name) as con:
        df.to_sql('airports', con, if_exists='replace', index=False)

# Main pipeline function
def main():
    df = download_data(DATA_URL)
    
    insert_data(df, 'airports.sqlite')

if __name__ == "__main__":
    main()
