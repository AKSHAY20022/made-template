import pandas as pd
import sqlite3

def load_and_preprocess_data(url):
    # Specify the index positions of the columns to keep
    cols_to_keep_indices = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]
    column_names = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']

    # Read the CSV file
    df = pd.read_csv(url, sep=';', encoding='latin-1', skiprows=6, usecols=cols_to_keep_indices, dtype={1: str})
    df.columns = column_names  # Set the column names
    df = df.iloc[:-4]  # Drop the last 4 rows

    # Validate CIN values
    df = df[df['CIN'].str.len() == 5]

    # Numeric columns
    numeric_cols = ['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']

    # Remove rows with '-' in numeric columns
    for col in numeric_cols:
        df = df[df[col] != '-']

    # Convert string values to integers and filter
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Drop rows with NaN (which were non-numeric values initially)
    df = df.dropna().query(' & '.join([f"{col} > 0" for col in numeric_cols]))

    return df

# Load data
df = load_and_preprocess_data('https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv')

# Save to SQLite database
conn = sqlite3.connect('cars.sqlite')
df.to_sql('cars', conn, if_exists='replace', index=False)
conn.close()
