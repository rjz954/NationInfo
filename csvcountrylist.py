import pandas as pd
import os

# Set the directory path to the dataset folder
dataset_path = os.path.join(os.getcwd(), 'dataset')

# Read the merged CSV file into a DataFrame
merged_df = pd.read_csv(os.path.join(dataset_path, 'schema_data.csv'))

# Drop duplicates based on 'T' column, keeping the first instance
filtered_df = merged_df.drop_duplicates(subset='Region/Country/Area', keep='first')

# Initialize a list to store the values
values = []

# Iterate through the filtered DataFrame
for index, row in filtered_df.iterrows():
    if pd.notna(row[1]):
        values.append(row[1])
    else:
        value_found = False
        # Iterate through columns starting from the 10th column
        for col_index in range(9, len(row)):
            if pd.notna(row[col_index]):
                values.append(row[col_index])
                value_found = True
                break
        if not value_found:
            values.append(None)

# Create a DataFrame with 'T' and the extracted values
result_df = pd.DataFrame({'id': filtered_df['Region/Country/Area'], 'value': values})

# Save the result to a new CSV file in the dataset folder
result_df.to_csv(os.path.join(dataset_path, 'Country_values.csv'), index=False)
