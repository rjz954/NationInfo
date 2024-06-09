import pandas as pd
import os
import psycopg2

# Database connection parameters
dbname = "countrydata"
user = "country_user"
password = "password"
host = "localhost"
port = "5432"

# SQL statement to create the table
create_table_query = """
CREATE TABLE IF NOT EXISTS Countries (
    id INT,
    Unnamed_1 TEXT,
    Year INT,
    Series TEXT,
    Capital_City TEXT,
    Capital_City_footnote TEXT,
    Value FLOAT,
    Footnotes TEXT,
    Source TEXT,
    System_of_trade TEXT,
    System_of_trade_footnote TEXT,
    National_currency TEXT,
    National_currency_footnote TEXT,
    Tourism_arrivals_series_type TEXT,
    Tourism_arrivals_series_type_footnote TEXT,
    Last_Election_Date TEXT,
    Last_Election_Date_footnote TEXT,
    Major_trading_partner_1_percent_of_exports TEXT,
    Major_trading_partner_1_percent_of_exports_footnote TEXT,
    PRIMARY KEY (id, Year, Series)
);
"""

# Connect to the PostgreSQL database
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cur = conn.cursor()

# Execute the SQL statement to create the table
cur.execute(create_table_query)
conn.commit()

# Read the CSV file into a DataFrame
csv_file_path = os.path.join('dataset', 'merged_data.csv')
data = pd.read_csv(csv_file_path)

# Define the insert query
insert_query = """
INSERT INTO Countries (
    id, Unnamed_1, Year, Series, Capital_City, Capital_City_footnote,
    Value, Footnotes, Source, System_of_trade, System_of_trade_footnote,
    National_currency, National_currency_footnote, Tourism_arrivals_series_type,
    Tourism_arrivals_series_type_footnote, Last_Election_Date, Last_Election_Date_footnote,
    Major_trading_partner_1_percent_of_exports, Major_trading_partner_1_percent_of_exports_footnote
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
)
"""

# Iterate over the DataFrame and insert data into the database
for _, row in data.iterrows():
    cur.execute(insert_query, tuple(row))

# Commit the transaction
conn.commit()

# Close communication with the database
cur.close()
conn.close()

print("Table 'Countries' created and data imported successfully.")