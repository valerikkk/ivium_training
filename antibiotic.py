import pandas as pd
import os

base_path = 'csv_ivium_new_data'
all_data = []

for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)
    for files in os.listdir(folder_path):
        path = os.path.join(folder_path, files)

        filename_component = [i for i in files.split('_')]

        df = pd.read_csv(path, sep=',').drop('Unnamed: 0', axis=1)
        df['Voltage, V'] = df['Voltage, V']
        df = df.set_index('Voltage, V').T.rename(index={'Current, A': 0})
        df['antibiotic'] = filename_component[0]
        df['concentration'] = float(filename_component[1])
        all_data.append(df)

big_data = pd.concat(all_data, ignore_index=True)
big_data.to_csv("ivium_data.csv", index_label='Voltage, V')