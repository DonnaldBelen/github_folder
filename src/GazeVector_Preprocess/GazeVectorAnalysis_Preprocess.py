print("Started")

import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly
import datetime
import glob

cwd = os.getcwd()

auto_open = False #choose True to display each plot, or False to just save them

###---
base_path = os.getcwd()
input_dirname = os.path.abspath(os.path.join(base_path,"..","..","input","GazeVector_Preprocess"))
filenames = sorted(glob.glob(input_dirname + "/*.csv"))
output_dirname = os.path.abspath(os.path.join(base_path,"..","..","output","GazeVector_Preprocess"))
out_folder = os.path.basename(os.path.abspath(os.path.join(filenames[0],"..")))
os.makedirs(output_dirname,exist_ok=True)

input_file = os.path.join(input_dirname,filenames[0])
csv_filepath = input_file
output_path = os.path.join(output_dirname,"count.csv")
#df = pd.read_csv(csv_filepath)
###---

KinectData_filepath = input_file
df_Kinect = pd.read_csv(KinectData_filepath,low_memory=False)#,index_col='sensing_time')
# print(df_Kinect.head())

plot_xyxt_filepath = os.path.join(output_dirname,'plot_xtyt.html')
plot_xy_filepath = os.path.join(output_dirname,'plot_xy.html')

df_out_path = os.path.join(output_dirname,'df_kinect.csv')

### Read and resample
# Read in Data, change to Datetime format, resample
df_Kinect = pd.read_csv(KinectData_filepath,low_memory=False)#,index_col='sensing_time')
df_Kinect.sensing_time = pd.to_datetime(df_Kinect.sensing_time)
df_Kinect.set_index('sensing_time',inplace=True) #INPLACE you fool!
df_Kinect = df_Kinect.resample('100L').last() # L = ms, so 100L = 100ms = 0.1s

# Unify Kinect and Tobii
df_unified = pd.DataFrame()
df_unified['Time'] = (df_Kinect.index)
df_unified['Sens_Time'] = (df_Kinect.index)
df_unified.set_index('Time',inplace=True) #INPLACE you fool!


df_unified['kinect_x'] = df_Kinect['data_fast_status_look_points_look_point_center_x']#+1200
df_unified['kinect_y'] = df_Kinect['data_fast_status_look_points_look_point_center_y']#+750

df_Kinect.to_csv(df_out_path)

##### Read and Clean Data - End #####

##### Plot Data X vs Y - Start #####

scatlayout = go.Layout(
    xaxis=dict(
        domain=[0, 1],
        title="Gaze X",
    ),
    yaxis=dict(
        title="Gaze Y",
        domain=[0, 1],
    ),
    title = "Gaze X vs Gaze Y",

)

scatfig = plotly.graph_objs.Figure(layout=scatlayout)

xaxis = 'x1'
yaxis = 'y1'
# Kinect Look Point
xdata = df_unified["kinect_x"]
ydata = df_unified["kinect_y"]
trace_kinect = plotly.graph_objs.Scatter(
    x = xdata,y= ydata,xaxis=xaxis,yaxis=yaxis,
    name="Kinect Look Point",
    mode="markers",
    marker=dict(size=5, symbol="square"),
    )
scatfig.add_trace(trace_kinect)

plotly.offline.plot(scatfig, filename = plot_xy_filepath, auto_open=auto_open) ###IMPORTANT

##### Plot Data X vs Y - End #####

##### Plot Data X vs Time and Y vs Time - Start #####
scatlayout_xt_yt = go.Layout(
    xaxis=dict(
        domain=[0, 1],
        title="Time",
        anchor="y2"
    ),
    yaxis1=dict(
        title="Gaze X",
        domain=[.52,1],
    ),
    yaxis2=dict(
        title="Gaze Y",
        domain=[0,.48],
    ),
    title = "Gazes vs Time",

)

scatfig_xyxt = plotly.graph_objs.Figure(layout=scatlayout_xt_yt)

xaxis = 'x1'
yaxis = 'y1'
# Kinect Look Point X vs t
xdata = df_unified["Sens_Time"]
ydata = df_unified["kinect_x"]
trace_kinect = plotly.graph_objs.Scatter(
    x = xdata,y= ydata,xaxis=xaxis,yaxis=yaxis,
    name="Kinect Look Points X",
    mode="markers",
    marker=dict(size=5, symbol="square"),
    )
scatfig_xyxt.add_trace(trace_kinect)

xaxis = 'x1'
yaxis = 'y2'
# Kinect Look Point Y vs t
xdata = df_unified["Sens_Time"]
ydata = df_unified["kinect_y"]
trace_kinect = plotly.graph_objs.Scatter(
    x = xdata,y= ydata,xaxis=xaxis,yaxis=yaxis,
    name="Kinect Look Points Y",
    mode="markers",
    marker=dict(size=5, symbol="square"),
    )
scatfig_xyxt.add_trace(trace_kinect)


plotly.offline.plot(scatfig_xyxt, filename = plot_xyxt_filepath,auto_open=auto_open)


print("Finished")
# Joint list: https://docs.microsoft.com/en-us/azure/kinect-dk/body-joints
