# Provides Value Counts for each column in a Dataframe #
# Input - DF to have repeat values counted #
# Output - CSV with 2 columns per input column
#           1) Value
#           2) Value counts
# To use enter: 1) csv_filepath - Input CSV
#               2) output_path - Output location for CSV to save

# Original Author: Nick Papa - 2020-12-01 #

print("Hello There")
print("General Kenobi")

import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly
import datetime
import glob

cwd = os.getcwd()

#Set the filepath for input CSV
# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 2 - Seat 3 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 2 - Seat 2 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 1 - Seat 3 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 1 - Seat 2 - Action.csv")

# output_path = os.path.join(cwd,"counts_Trial2_Seat3.csv")
# output_path = os.path.join(cwd,"counts_Trial2_Seat2.csv")
# output_path = os.path.join(cwd,"counts_Trial1_Seat3.csv")
# output_path = os.path.join(cwd,"counts_Trial1_Seat2.csv")

###---
base_path = os.getcwd()
input_dirname = os.path.abspath(os.path.join(base_path,"..","..","input","ColumnCounts"))
filenames = sorted(glob.glob(input_dirname + "/*.csv"))
output_dirname = os.path.abspath(os.path.join(base_path,"..","..","output","ColumnCounts"))
out_folder = os.path.basename(os.path.abspath(os.path.join(filenames[0],"..")))
os.makedirs(output_dirname,exist_ok=True)

input_file = os.path.join(input_dirname,filenames[0])
csv_filepath = input_file
output_path = os.path.join(output_dirname,"count.csv")
df = pd.read_csv(csv_filepath)
###---

df_counts = pd.DataFrame(dtype=object) #open the df

col_list = df.columns #list of columns in the dataframe

k=0
while(k< len(col_list)): #for each column, get the counts and add to df_counts

    col_name = col_list[k]

    count = df[col_name].value_counts()

    col_name_val = col_name + "_VAL"
    col_name_count = col_name + "_COUNT"

    df_int = count.to_frame()
    df_int=df_int.reset_index()

    df_counts[col_name_val] = df_int['index']
    df_counts[col_name_count] = df_int[col_name]
    k+=1

df_counts.to_csv(output_path)

print("Done")
