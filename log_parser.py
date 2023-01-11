#!/usr/bin/env python
# coding: utf-8

# In[546]:


import numpy as np
import pandas as pd

print('[INFO] numpy version:', np.version.full_version)
print('[INFO] pandas version:', pd.__version__)


# In[548]:


# Settings
pd.set_option('display.max_columns', None)


# In[588]:


# import the necessary packages
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", type=str, default="./data/detections023 2.txt", help="path to input file")
ap.add_argument("-o", "--output", type=str, required=False, help="output file (must include full path)")

args = vars(ap.parse_args())


# In[589]:


def get_input_file_path():
    print("[INFO] Get input/output parameters")
    
    from pathlib import Path

    file_path = args['file']
    path = Path(file_path)

    if path.is_file() == False:
        raise Exception("File does not exist!")

    print(f"[INFO] File: {file_path}")

    filename = path.stem
    suffix = path.suffix
    dir = path.parent

    return {
        'full_file_path': file_path,
        'filename': filename,
        'suffix': suffix,
        'path': dir
    }


# In[590]:


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

def save_to_csv(full_file_path, filename, suffix, path):
    
    output = args['output']
    if(output is None):
        output = f'{path}/{filename}.csv'

    print('[INFO] Saving CSV in', output)

    selected_columns = df.columns.to_series().filter(regex='^(?!Field).*$')

    df[selected_columns].to_csv(output)    
        


# In[592]:


try:
    print('[INFO] Starting parsing file')
    
    fields = ["Analyzer-Instance", "Field-2", "Date", "Time", "Field-5", "Field-6", "Field-7", "Field-8",
              "Field-9", "Field-10", "Field-11", "Field-12", "Field-13", "Field-14", "JobId", 
              "Markers", "Field-17", "Field-18"]
    
    input_file_path = get_input_file_path()
    
    df = pd.read_csv(input_file_path['full_file_path'], sep='\s+', header=None, index_col=None, names=fields)

    # Format fields
    format_date_time()
    formar_local_manager()    
    df = split_markers(df)
    save_to_csv(**input_file_path)
except Exception as inst:
    print("[ERROR]", inst)