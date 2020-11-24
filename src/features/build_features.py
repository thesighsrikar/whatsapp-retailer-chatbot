# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:19:37 2020

@author: Srikar

NOTE: When migrating to another Directory, change "mypath" and "export_path" variables 
"""
import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join

mypath = r'D:\whatsapp-retailer-chatbot\data\raw\BigBasket-RawDataset'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

export_path = r'D:\whatsapp-retailer-chatbot\data\interim\BigBasket-CleanedDataset_Intermediate'

# Totally ignore this section since there will be pharmacies for this. 
# Their demand will not decrease whene compared to other items.
onlyfiles.remove('BB_health-medicine.csv')

cols_name = ['product-name', 'mrp', 'selling-price', 'num-of-ratings', 'discount (%)', 
        'brand', 'rating', 'combos', 'quantity-display'] # A list of all the important columns
int_cols = ['selling-price', 'num-of-ratings', 'mrp', 'discount (%)', 'rating']

for i in range(len(onlyfiles)):
    # Open a file
    df = pd.read_csv(mypath + '\\' + onlyfiles[i])
    print(onlyfiles[i])
    # Assuming that all the CSV files have the required names of the columns
    # Extracting only the required and dropping the remaining
    df.drop(df.columns.difference(cols_name), axis=1, inplace=True) 
    
    # Cleaning all the entries. Getting rid of ["XXXX"]   
    df_clean = df.replace(r'["\["\]]', '', regex=True)
    
    if ((onlyfiles[i] == 'BB_eggs-meat-fish.csv') | 
            (onlyfiles[i] == 'BB_fruits-vegetables.csv')):
        df_clean['selling-price'] = df_clean['selling-price'].astype('float64')
        df_clean['mrp'] = df_clean['mrp'].astype(np.float64)
        df_clean['discount (%)'] = df_clean['discount (%)'].astype('float64')
    else:
        # Typecasting the columns required
        df_clean['selling-price'] = df_clean['selling-price'].astype('float64')
        df_clean['num-of-ratings'] = df_clean['num-of-ratings'].astype('float64')
        df_clean['mrp'] = df_clean['mrp'].astype('float64')
        df_clean['discount (%)'] = df_clean['discount (%)'].astype('float64')
        df_clean['rating'] = df_clean['rating'].astype('float64')
    
    # Filling the missing values in 'mrp' column
    df_clean.mrp.fillna(df_clean['selling-price'], inplace=True)
    df_clean['discount (%)'].fillna(0, inplace=True)
    
    # Remove the items which are of BigBasket brand. Temporarily disabled 
    # df_clean.loc[~df_clean['brand'].isin(['bb Royal', 'bb Combo'])]
    
    df_clean.to_csv(export_path + '\\' + onlyfiles[i], index=False, header=True)