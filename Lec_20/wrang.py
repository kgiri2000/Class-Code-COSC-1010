# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:27:10 2021

@author: kgiri
"""

#!/Users/philip/opt/anaconda3/bin/python

import numpy as np
import pandas as pd
import re
# import matplotlib.pyplot as plt
# import seaborn as sns

# import tensorflow as tf

# import tensorflow_docs as tfdocs
# import tensorflow_docs.plots
# import tensorflow_docs.modeling

dataset_path = "./train-data.csv"

column_names = ['Ind', 'Name', 'Location', 'Year', 'Kilometers_Driven',
    'Fuel_Type', 'Transmission', 'Owner_Type', 'Mileage', 'Engine',
    'Power', 'Seats', 'New_Price', 'Price']
raw_dataset = pd.read_csv(dataset_path, names=column_names,
    na_values = "?", comment='\t', skiprows=1, sep=",",
    skipinitialspace=True)

dataset = raw_dataset.copy()

print("\n\n\n\n\n New Code \n\n\n\n\n ") 
print ( dataset.head() )










# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html

dataset = dataset.drop(columns=['Ind', 'Name', 'Location', 'Seats', 'New_Price'])





print(" \n\n\n\n\n New Code1\n\n\n\n\n")
print ( dataset.head() )

# To see a good description of the dataset




print(" \n\n\n\n\n New Code2 \n\n\n\n\n")
print ( dataset.describe() )

# Cleaning the data
# The dataset contains a few unknown values. Let’s find them and drop them.

dataset.isna().sum()
dataset = dataset.dropna()
dataset = dataset.reset_index(drop=True)


print(" \n\n\n\n\n New Code3 \n\n\n\n\n")
print ( dataset.head() )


dataset['Mileage'] = pd.Series([re.sub('[^.0-9]', '',
    str(val)) for val in dataset['Mileage']], index = dataset.index)
dataset['Engine'] = pd.Series([re.sub('[^.0-9]', '',
    str(val)) for val in dataset['Engine']], index = dataset.index)
dataset['Power'] = pd.Series([re.sub('[^.0-9]', '',
    str(val)) for val in dataset['Power']], index = dataset.index)

# The prices are by default in INR Lakhs. So, we have to convert them to USD

dataset['Price'] = pd.Series([int(float(val)*1521.22) for val in dataset['Price']], index = dataset.index)


print(" \n\n\n\n\n New Code4 \n\n\n\n\n ")
print ( dataset.head() )

dataset = dataset.replace(r'^\s*$', np.nan, regex=True)
dataset.isna().sum()
dataset = dataset.dropna()

dataset = dataset.reset_index(drop=True)

print(" \n\n\n\n\n New Code5 \n\n\n\n\n ")
print ( dataset.head() )

# Next, we’ll convert the strings in the below columns into float values. Remember that we can only work with numerical values.

## dataset['Mileage'] = pd.Series([int(float(str(val))*2.3521458) for val in dataset['Mileage']], index = dataset.index)
dataset['Mileage'] = pd.Series([int(float(str(val))*2.3521458) for val in dataset['Mileage']], index = dataset.index)
dataset['Engine'] = pd.Series([float(str(val)) for val in dataset['Engine']], index = dataset.index)
dataset['Power'] = pd.Series([float(val) for val in dataset['Power']], index = dataset.index)
## dataset['Miles_Driven'] = pd.Series([str(int(float(val)*0.621371))+" mpg" for val in dataset['Kilometers_Driven']], index = dataset.index)
dataset['Miles_Driven'] = pd.Series([(int(float(val)*0.621371)) for val in dataset['Kilometers_Driven']], index = dataset.index)
# dataset['Kilometers_Driven'] = pd.Series([float(val) for val in dataset['Kilometers_Driven']], index = dataset.index)
dataset = dataset.drop(columns=['Kilometers_Driven'])


print(" \n\n\n\n\n New Code6 \n\n\n\n\n ")
print ( dataset.head() )

dataset.to_csv(path_or_buf="new-car-data.csv")

#  Year  Kilometers_Driven Fuel_Type Transmission Owner_Type  Mileage  Engine   Power  Price
# 1. Kilometers_Driven -> Miles_Driven
# 2. Milage is in kmpl (Km Per Leter) -> convert to Mi per Gal


## One-Hot the Fule_Type

print(" \n\n\n\n\n New Code7 \n\n\n\n\n ")
print(dataset['Fuel_Type'].unique())
dataset['Fuel_Type'] = pd.Categorical(dataset['Fuel_Type'])
dfFuel_Type = pd.get_dummies(dataset['Fuel_Type'], prefix = 'Fuel_Type')

print(" \n\n\n\n\n New Code8 \n\n\n\n\n ")
print ( dfFuel_Type.head() )

## One-Hot the Transmission
print(" \n\n\n\n\n New Code9 \n\n\n\n\n ")
print(dataset['Transmission'].unique())
dataset['Transmission'] = pd.Categorical(dataset['Transmission'])
dfTransmission = pd.get_dummies(dataset['Transmission'], prefix = 'Transmission')

print(" \n\n\n\n\n New Code10 \n\n\n\n\n ")
print ( dfTransmission.head() )

## One-Hot the Owner


print(" \n\n\n\n\n New Code11 \n\n\n\n\n")
print(dataset['Owner_Type'].unique())
dataset['Owner_Type'] = pd.Categorical(dataset['Owner_Type'])
dfOwner_Type = pd.get_dummies(dataset['Owner_Type'], prefix = 'Owner_Type')

print(" \n\n\n\n\n New Code12 \n\n\n\n\n ")
print ( dfOwner_Type.head() )

## Concat it all together

dataset = pd.concat([dataset, dfFuel_Type, dfTransmission, dfOwner_Type], axis=1)
dataset = dataset.drop(columns=['Owner_Type', 'Transmission', 'Fuel_Type'])

print(" \n\n\n\n\n New Code13 \n\n\n\n\n ")
print ( dataset.head() )


dataset.to_csv(path_or_buf="new-car-data2.csv")