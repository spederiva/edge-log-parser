#!/usr/bin/env python
# coding: utf-8

from pathlib import Path

path = Path("./data/detections023 2.txt")

print(path.is_file())

filename = path.stem
suffix = path.suffix
dir = path.parent

print(filename)
print(suffix)
print(dir)

# In[546]:


import numpy as np
import pandas as pd

print('[INFO] numpy version:', np.version.full_version)
print('[INFO] pandas version:', pd.__version__)


# In[544]:


# Settings
pd.set_option('display.max_columns', None)

# In[483]:


# import the necessary packages
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", type=str, default="./detections023 2.txt", help="path to input file")


args = vars(ap.parse_args())
file_path = args['file']

print(f"[INFO] File: {file_path}")


# In[533]:


def format_date_time():
    print('[INFO] Converting Date/Time to EPOCH')
    
    df['Date-epoch'] = (pd.to_datetime(df["Date"] + " " + df["Time"]).astype('int64') // 1e6).astype('int')
    
def add_markers_length():
    df['markers-length'] = df['Markers'].str.len()
    
def split_markers():
    print('split')
    
    # count number of max markers
    biggest_markers = df.sort_values(by=['markers-length'], inplace=False, ascending=False)[0]['Markers']
    
    print(biggest_markers)

def formar_local_manager():
    df['Analyzer-Instance'] = df['Analyzer-Instance'].str.replace('.*_', '', regex=True)
    
def split_markers(df):
    print('[INFO] Splitting "Markers" in fields')
    
    mm = df['Markers'].str.strip(to_strip='()').str.split('\)\(', expand=True)

    df1 = df
    
    for col in mm.columns:
        cols_marker = mm[col].str.strip(to_strip=']').str.split('\[|,', expand=True, regex=True).rename(columns={0:f'Marker-{col}', 1:f'Marker-{col}-X', 2:f'Marker-{col}-Y'})

        df1 = df1.join(cols_marker)
        
    return df1

def save_to_csv():
    print('[INFO] Saving CSV')
    
    selected_columns = df.columns.to_series().filter(regex='^(?!Field).*$')

    df[selected_columns].to_csv('./sample.csv')    
        


# In[534]:


try:
    print('[INFO] Starting parsing file')
    
    fields = ["Analyzer-Instance", "Field-2", "Date", "Time", "Field-5", "Field-6", "Field-7", "Field-8",
              "Field-9", "Field-10", "Field-11", "Field-12", "Field-13", "Field-14", "JobId", 
              "Markers", "Field-17", "Field-18"]

    df = pd.read_csv(file_path, sep='\s+', header=None, index_col=None, names=fields)

    # Format fields
    format_date_time()
    formar_local_manager()    
    df = split_markers(df)
    save_to_csv()
except Exception as inst:
    print("[ERROR]", inst)