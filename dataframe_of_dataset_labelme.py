import os
import json

import pandas as pd
import numpy as np
from label_frequency import return_class_set

input_dir = input("Enter path to input directory: ")

files = list()
class_names = list(return_class_set(os.path.join(input_dir,'train')))
class_names.insert(0,'split')
# print(class_names)
df = pd.DataFrame(index=[], columns=class_names)
# Iterate through each split directory
for directory in ('train', 'test', 'val'):
    for file in os.listdir(os.path.join(input_dir, directory)):
        if file.endswith('.json'):
            file_name = file.split('.')[0]

            files.append(file_name)
            # Populate the DataFrame with 'split' and class names
            df.loc[file_name, 'split'] = directory
            label_file = open(os.path.join(input_dir, directory, file), 'r')
            data = json.load(label_file)
            for shape in data['shapes']:
                class_name = shape['label']


df.fillna(0, inplace=True)
# print(df)

for directory in ('train', 'test', 'val'):
    for file in os.listdir(os.path.join(input_dir, directory)):
        if file.endswith('.json'):
            file_name = file.split('.')[0]

            files.append(file_name)
            # Populate the DataFrame with 'split' and class names
            df.loc[file_name, 'split'] = directory
            label_file = open(os.path.join(input_dir, directory, file), 'r')
            data = json.load(label_file)
            for shape in data['shapes']:
                class_name = shape['label']
                df.loc[file_name,class_name]+=1
df.to_csv(r'./dataset_dataframe.csv')
# df = pd.DataFrame(0, index=files, columns=list(return_class_set(input_dir)))

