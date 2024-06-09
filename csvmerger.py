import pandas as pd
import os


def remove_commas_from_value(value):
    if isinstance(value, str) and ',' in value:
        return value.replace(',', '')
    return value


current_directory = os.getcwd()


dataset_path = os.path.join(current_directory, 'dataset')


csv_files = [os.path.join(dataset_path, file) for file in os.listdir(dataset_path) if file.endswith('.csv')]


dfs = []


for file in csv_files:
    df = pd.read_csv(file, encoding='latin-1')
    if 'Value' in df.columns:
        df['Value'] = df['Value'].apply(remove_commas_from_value)
    dfs.append(df)


merged_df = pd.concat(dfs, ignore_index=True)


merged_df.to_csv(os.path.join(dataset_path, 'merged_data.csv'), index=False, header=False)


merged_df.to_csv(os.path.join(dataset_path, 'schema_data.csv'), index=False)
