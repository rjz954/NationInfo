import pandas as pd
import os


dataset_path = os.path.join(os.getcwd(), 'dataset')


merged_df = pd.read_csv(os.path.join(dataset_path, 'schema_data.csv'))


filtered_df = merged_df.drop_duplicates(subset='Region/Country/Area', keep='first')


values = []


for index, row in filtered_df.iterrows():
    if pd.notna(row[1]):
        values.append(row[1])
    else:
        value_found = False
        for col_index in range(9, len(row)):
            if pd.notna(row[col_index]):
                values.append(row[col_index])
                value_found = True
                break
        if not value_found:
            values.append(None)


result_df = pd.DataFrame({'id': filtered_df['Region/Country/Area'], 'value': values})


result_df.to_csv(os.path.join(dataset_path, 'Country_values.csv'), index=False)
