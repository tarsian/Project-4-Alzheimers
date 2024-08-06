# load_data.py

import pandas as pd
import sqlite3

# Read the CSV file into a DataFrame
df = pd.read_csv('../Resources/alzheimers_disease_data.csv')

# Connect to the SQLite database (creates database if it does not exist)
conn = sqlite3.connect('alzheimers.db')

# Save the DataFrame to an SQL table
df.to_sql('alzheimers_data', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

print("CSV file has been uploaded!")
