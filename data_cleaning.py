import os

import pandas as pd
import numpy as np

df = pd.read_csv('df_1_arabica.csv')
df.info()

df.rename(columns={df.columns[0]: 'ID'}, inplace=True) # changing the uninformative first column to ID
df['ID'] = pd.Series(range(df.shape[0])) # assigning the ID numbers

df.drop('NA', axis='columns', inplace=True) # dropping the NA columns. It's just NA.

df['Color'] = df['Color'].str.lower() # for consistent wording

df['Category One Defects'] = df['Category One Defects'].str.split(' ', 1, expand=True)[0] # only numeric values
df['Category Two Defects'] = df['Category Two Defects'].str.split(' ', 1, expand=True)[0] # only numeric values

df.rename(columns={'Moisture': 'Moisture Percentage'}, inplace=True) # this variable is in percentage, changing the name
df['Moisture Percentage'] = df['Moisture Percentage'].str.split(' ', 1, expand=True)[0] # only numeric values

df.to_csv('df_arabica_clean.csv')