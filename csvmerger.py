import pandas as pd
import os

# Function to remove commas from numeric values in the "Value" column
def remove_commas_from_value(value):
    if isinstance(value, str) and ',' in value:
        return value.replace(',', '')
    return value

# Get the current directory
current_directory = os.getcwd()

# Set the directory path to the dataset folder
dataset_path = os.path.join(current_directory, 'dataset')

# List all CSV files in the dataset directory
csv_files = [os.path.join(dataset_path, file) for file in os.listdir(dataset_path) if file.endswith('.csv')]

# Initialize an empty list to store DataFrames
dfs = []

# Read each CSV file with Latin-1 encoding and append to dfs list
for file in csv_files:
    df = pd.read_csv(file, encoding='latin-1')

    # Remove commas from the "Value" column
    if 'Value' in df.columns:
        df['Value'] = df['Value'].apply(remove_commas_from_value)

    dfs.append(df)

# Concatenate all DataFrames in dfs list into a single DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged dataframe to a new CSV file without column names in the dataset folder
merged_df.to_csv(os.path.join(dataset_path, 'merged_data.csv'), index=False, header=False)

# Save the merged dataframe to another CSV file with column names in the dataset folder
merged_df.to_csv(os.path.join(dataset_path, 'schema_data.csv'), index=False)
