import pandas as pd
import os

# List all CSV files in the directory
csv_files = [file for file in os.listdir() if file.endswith('.csv')]

# Initialize an empty list to store DataFrames
dfs = []

# Read each CSV file with Latin-1 encoding and append to dfs list
for file in csv_files:
    df = pd.read_csv(file, encoding='latin-1')
    dfs.append(df)

# Concatenate all DataFrames in dfs list into a single DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged dataframe to a new CSV file
merged_df.to_csv('merged_data.csv', index=False)
