import pandas as pd
import os

# Set the directory path to the dataset folder
dataset_path = os.path.join(os.getcwd(), 'dataset')

# Read the merged CSV file into a DataFrame
merged_df = pd.read_csv(os.path.join(dataset_path, 'schema_data.csv'))

# Extract unique instances of the 'series' column without duplicates
unique_series = merged_df['Series'].drop_duplicates()

# Create a DataFrame with the unique instances of the 'series' column
result_df = pd.DataFrame({'Series': unique_series})

# Save the result to a new CSV file in the dataset folder
result_df.to_csv(os.path.join(dataset_path, 'Unique_series.csv'), index=False)
