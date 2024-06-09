import pandas as pd
import os


dataset_path = os.path.join(os.getcwd(), 'dataset')


merged_df = pd.read_csv(os.path.join(dataset_path, 'schema_data.csv'))


unique_series = merged_df['Series'].drop_duplicates()


result_df = pd.DataFrame({'Series': unique_series})


result_df.to_csv(os.path.join(dataset_path, 'Unique_series.csv'), index=False)
