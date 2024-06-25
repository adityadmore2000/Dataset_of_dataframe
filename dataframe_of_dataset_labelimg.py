import os

import pandas as pd

input_dir = input("Enter path to input directory: ")

files = list()
class_names = ["basin", "toilet_bowl", "bathtub", "roof_ac", "smoke_detector", "lamp1", "lamp2", "ac_vent", "lamp3",
               "wall_ac", "fire_hydrant", "pump", "generator", "transformer", "pump_stand"]
class_names.insert(0, 'split')
# print(class_names)
df = pd.DataFrame(index=[], columns=class_names)

mappping = {'0':"basin", '1': "toilet_bowl", '2':"bathtub", '3':"roof_ac", '4': "smoke_detector", '5':"lamp1", '6':"lamp2",'7': "ac_vent",'8': "lamp3",
               '9':"wall_ac", '10':"fire_hydrant", '11':"pump", '12':"generator", '13':"transformer", '14':"pump_stand"}
# Iterate through each split directory
for directory in ('train', 'test', 'val'):
    for file in os.listdir(os.path.join(input_dir, directory)):
        if file.endswith('.txt'):
            file_name = file.split('.')[0]

            files.append(file_name)
            # Populate the DataFrame with 'split' and class names
            df.loc[file_name, 'split'] = directory
            label_file = os.path.join(input_dir, directory, file)


df.fillna(0, inplace=True)
# print(df)

for directory in ('train', 'test', 'val'):
    for file in os.listdir(os.path.join(input_dir, directory)):
        if file.endswith('.txt')  and file!='classes.txt':
            file_name = file.split('.')[0]

            files.append(file_name)
            # Populate the DataFrame with 'split' and class names
            df.loc[file_name, 'split'] = directory
            label_file = open(os.path.join(input_dir, directory, file), 'r')
            df.loc[file_name, 'split'] = directory
            label_file = os.path.join(input_dir, directory, file)
            with open(label_file) as f:
                for line in f:
                    class_name = mappping[line[0:2].strip()]
                    df.loc[file_name,class_name]+=1
df.to_csv(r'./dataset_dataframe_mep.csv')
# df = pd.DataFrame(0, index=files, columns=list(return_class_set(input_dir)))
