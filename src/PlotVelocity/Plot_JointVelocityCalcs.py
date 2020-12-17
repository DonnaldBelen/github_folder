#Calculate angular velocity of gaze direction

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

cwd=os.getcwd()

###---
base_path = os.getcwd()
input_dirname = os.path.abspath(os.path.join(base_path,"..","..","input","PlotVelocity"))
filenames = sorted(glob.glob(input_dirname + "/*.csv"))
output_dirname = os.path.abspath(os.path.join(base_path,"..","..","output","PlotVelocity"))
out_folder = os.path.basename(os.path.abspath(os.path.join(filenames[0],"..")))
os.makedirs(output_dirname,exist_ok=True)

input_file = os.path.join(input_dirname,filenames[0])
csv_filepath = input_file
df = pd.read_csv(csv_filepath)
###---

output_path1 = os.path.join(output_dirname,"Velocities_1.html")
output_path2 = os.path.join(output_dirname,"Velocities_2.html")
output_path3 = os.path.join(output_dirname,"Velocities_3.html")


title = "Velocity Over Time"
# csv_filepath = os.path.join(cwd,"df_Velocity","df_Vel_kinectTrial 2 - Seat 3 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_Velocity","df_Vel_kinectTrial 2 - Seat 2 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_Velocity","df_Vel_kinectTrial 1 - Seat 3 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_Velocity","df_Vel_kinectTrial 1 - Seat 2 - Action.csv")
df = pd.read_csv(csv_filepath)

title = "Joint Velocity"

scatlayout = go.Layout(
    xaxis=dict(
        domain=[0, 1],
        title="Sensing Time (s)",
    ),
    yaxis=dict(
        title="Velocity (mm/s) ",
        domain=[0, 1],
    ),
    title = title,
)
scatfig = plotly.graph_objs.Figure(layout=scatlayout)


plotthese1 = ['vel_Neck','vel_Head','vel_Nose','vel_Leye','vel_Reye','vel_Lear','vel_Rear']
plotthese2 = ['vel_Sum_Joints']
plotthese3 = ['vel_Hfacedir','vel_Vfacedir','vel_FaceDir_combined']

################ PLOT 1 #####################

for things in plotthese1:
    print(things)
    things_mov10 = things + '_mov10'

    xaxis = 'x1'
    yaxis = 'y1'
    # Kinect Look Point
    xdata = df["sensing_time"]
    ydata = df[things]
    trace_kinect = plotly.graph_objs.Scatter(
        x = xdata,y= ydata,xaxis=xaxis,yaxis=yaxis,
        name=things,
        mode="markers",
        marker=dict(size=3, symbol="circle"),
        )
    scatfig.add_trace(trace_kinect)

    xaxis = 'x1'
    yaxis = 'y1'
    # Kinect Look Point
    xdata = df["sensing_time"]
    ydata = df[things_mov10]
    trace_kinect = plotly.graph_objs.Scatter(
        x = xdata,y= ydata,xaxis=xaxis,yaxis=yaxis,
        name=things_mov10,
        mode="lines",
        # marker=dict(size=3, symbol="circle"),
        )
    scatfig.add_trace(trace_kinect)

plot_filepath = os.path.join(cwd,title+"_VelPlot_Joints.html")
plotly.offline.plot(scatfig, filename = output_path1,auto_open=True)

################ PLOT 2 #####################
scatfig2 = plotly.graph_objs.Figure(layout=scatlayout)

for things in plotthese2:
    # print(things)
    things_mov10 = things + '_mov10'

    xaxis = 'x1'
    yaxis = 'y1'
    # Kinect Look Point
    xdata = df["sensing_time"]
    ydata = df[things]
    trace_kinect = plotly.graph_objs.Scatter(
        x = xdata,y= ydata,xaxis=xaxis,yaxis=yaxis,
        name=things,
        mode="markers",
        marker=dict(size=3, symbol="circle"),
        )
    scatfig2.add_trace(trace_kinect)

    xaxis = 'x1'
    yaxis = 'y1'
    # Kinect Look Point
    xdata = df["sensing_time"]
    ydata = df[things_mov10]
    trace_kinect = plotly.graph_objs.Scatter(
        x = xdata,y= ydata,xaxis=xaxis,yaxis=yaxis,
        name=things_mov10,
        mode="lines",
        # marker=dict(size=3, symbol="circle"),
        )
    scatfig2.add_trace(trace_kinect)

plot_filepath = os.path.join(cwd,title+"_VelPlot2_SumJoints.html")
plotly.offline.plot(scatfig2, filename = output_path2,auto_open=True)


################ PLOT 3 #####################
scatfig3 = plotly.graph_objs.Figure(layout=scatlayout)
for things in plotthese3:
    print(things)
    things_mov10 = things + '_mov10'

    xaxis = 'x1'
    yaxis = 'y1'
    # Kinect Look Point
    xdata = df["sensing_time"]
    ydata = df[things]
    trace_kinect = plotly.graph_objs.Scatter(
        x = xdata,y= ydata,xaxis=xaxis,yaxis=yaxis,
        name=things,
        mode="markers",
        marker=dict(size=3, symbol="circle"),
        )
    scatfig3.add_trace(trace_kinect)

    xaxis = 'x1'
    yaxis = 'y1'
    # Kinect Look Point
    xdata = df["sensing_time"]
    ydata = df[things_mov10]
    trace_kinect = plotly.graph_objs.Scatter(
        x = xdata,y= ydata,xaxis=xaxis,yaxis=yaxis,
        name=things_mov10,
        mode="lines",
        # marker=dict(size=3, symbol="circle"),
        )
    scatfig3.add_trace(trace_kinect)

plot_filepath = os.path.join(cwd,title+"_VelPlot3_Gazes.html")
plotly.offline.plot(scatfig3, filename = output_path3,auto_open=True)



################ End Block #####################
Timeend = datetime.now()
TimeTaken = Timeend - Timestart
print("Time: " + str(TimeTaken) + " seconds")
print("DONE")
