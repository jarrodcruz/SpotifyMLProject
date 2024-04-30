""" Author: Jarrod Cruz
    Description: Utilizing song data from Spotify in 2023
"""

import numpy as np
import pandas as pd

raw_data = pd.read_csv('spotify-2023.csv',encoding='ISO-8859-1')

raw_data.head()
raw_data.info()

na = raw_data.isna() 
na_val_in_col = na.any()

# iterate through columns to get frequency of missing values
for col, na_present in na_val_in_col.items():
    if na_present:
        curr_freq = raw_data.isnull().sum()[col]
        print(f"{curr_freq} missing values in column '{col}'.")

raw_data = raw_data.dropna(subset=['key'])

raw_data = raw_data.dropna(subset = ['in_shazam_charts'])
