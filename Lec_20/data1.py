# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 17:26:18 2021

@author: kgiri
"""

#!/Users/philip/opt/anaconda3/bin/python

import numpy as np
import pandas as pd
import re

dataset_path = "./train-data.csv"

column_names = ['Ind', 'Name', 'Location', 'Year', 'Kilometers_Driven',
    'Fuel_Type', 'Transmission', 'Owner_Type', 'Mileage', 'Engine',
    'Power', 'Seats', 'New_Price', 'Price']
raw_dataset = pd.read_csv(dataset_path, names=column_names,
    na_values = "?", comment='\t', skiprows=1, sep=",",
    skipinitialspace=True)

dataset = raw_dataset.copy()
print ( dataset.head() )

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html

dataset = dataset.drop(columns=['Ind', 'Name', 'Location', 'Seats', 'New_Price'])
print ( dataset.head() )

# To see a good description of the dataset

print ( dataset.describe() )
