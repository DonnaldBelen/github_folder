#Basic, Quick Plot - Omega Array

import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly
import datetime
import matplotlib
import matplotlib.pyplot as plt
import math
import glob

import matplotlib.animation as animation

from datetime import datetime #Just to track the amount of time it takes to plot

Timestart = datetime.now()
print("Start: " + str(Timestart))

###---
base_path = os.getcwd()
input_dirname = os.path.abspath(os.path.join(base_path,"..","..","input","PlotAngularVelocity"))
filenames = sorted(glob.glob(input_dirname + "/*.csv"))
output_dirname = os.path.abspath(os.path.join(base_path,"..","..","output","PlotAngularVelocity"))
out_folder = os.path.basename(os.path.abspath(os.path.join(filenames[0],"..")))
os.makedirs(output_dirname,exist_ok=True)

input_file = os.path.join(input_dirname,filenames[0])
csv_filepath = input_file
df = pd.read_csv(csv_filepath)
###---

output_path = os.path.join(output_dirname,"AngularVelocities.html")


title = "Angular Velocity Over Time"

# csv_filepath = os.path.join(cwd,"df_AngularVelocity","df_AngVel_kinectTrial 2 - Seat 3 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_AngularVelocity","df_AngVel_kinectTrial 2 - Seat 2 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_AngularVelocity","df_AngVel_kinectTrial 1 - Seat 3 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_AngularVelocity","df_AngVel_kinectTrial 1 - Seat 2 - Action.csv")


#plot_filepath = os.path.join(base_path,"Trial 1 - Seat 2_AngularVelocity.html")
plot_filepath = output_path

df = pd.read_csv(csv_filepath)

# df = df.reset_index()
# df['times']=df['index']*(0.1) #Technically lazy way because I know its 0.1s increments
# tvals = df['sensing_time'] #time values
xvals = df['sensing_time']
yvals = df['omega_array']


scatlayout = go.Layout(
    xaxis=dict(
        domain=[0, 1],
        title="Sensing Time (s)",
    ),
    yaxis=dict(
        title="ω - Angular Velocity (deg/s) ",
        domain=[0, 1],
    ),
    title = title,
)
scatfig = plotly.graph_objs.Figure(layout=scatlayout)

xaxis = 'x1'
yaxis = 'y1'
# Kinect Look Point
xdata = df["sensing_time"]
ydata = df["omega_deg"]
trace_kinect = plotly.graph_objs.Scatter(
    x = xdata,y= ydata,xaxis=xaxis,yaxis=yaxis,
    name="Angular Velocity",
    mode="markers",
    marker=dict(size=3, symbol="circle"),
    )
scatfig.add_trace(trace_kinect)

xaxis = 'x1'
yaxis = 'y1'
# Kinect Look Point
xdata = df["sensing_time"]
ydata = df["MovingAvg_omega_deg"]
trace_kinect = plotly.graph_objs.Scatter(
    x = xdata,y= ydata,xaxis=xaxis,yaxis=yaxis,
    name="10 Moving Avg",
    mode="lines",
    # marker=dict(size=3, symbol="circle"),
    )
scatfig.add_trace(trace_kinect)

xaxis = 'x1'
yaxis = 'y1'
# Kinect Look Point
xdata = df["sensing_time"]
ydata = df["MovingAvg50_omega_deg"]
trace_kinect = plotly.graph_objs.Scatter(
    x = xdata,y= ydata,xaxis=xaxis,yaxis=yaxis,
    name="50 Moving Avg",
    mode="lines",
    # marker=dict(size=3, symbol="circle"),
    )
scatfig.add_trace(trace_kinect)



plotly.offline.plot(scatfig, filename = plot_filepath,auto_open=True)

# print(math.pi)
