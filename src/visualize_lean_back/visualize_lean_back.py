#!/usr/bin/python3
print("Started")

import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly
import datetime
import glob
import sys

cwd = os.getcwd()

auto_open = int(sys.argv[2])
print(sys.argv[2])

columns_2 = ["data_seat2_joints_0_position_0",
"data_seat2_joints_0_position_1",
"data_seat2_joints_0_position_2",
"data_seat2_joints_1_position_0",
"data_seat2_joints_1_position_1",
"data_seat2_joints_1_position_2",
"data_seat2_joints_2_position_0",
"data_seat2_joints_2_position_1",
"data_seat2_joints_2_position_2",
"data_seat2_joints_3_position_0",
"data_seat2_joints_3_position_1",
"data_seat2_joints_3_position_2"]

columns_3 = ["data_seat3_joints_0_position_0",
"data_seat_joints_0_position_1",
"data_seat3_joints_0_position_2",
"data_seat3_joints_1_position_0",
"data_seat3_joints_1_position_1",
"data_seat3_joints_1_position_2",
"data_seat3_joints_2_position_0",
"data_seat3_joints_2_position_1",
"data_seat3_joints_2_position_2",
"data_seat3_joints_3_position_0",
"data_seat3_joints_3_position_1",
"data_seat3_joints_3_position_2"]

column_header = ["PELVIS",
"PELVIS",
"PELVIS",
"NAVAL",
"NAVAL",
"NAVAL",
"CHEST",
"CHEST",
"CHEST",
"NECK",
"NECK",
"NECK"]

seat_header = ["seat2", "seat3"]

targ_column = int(sys.argv[1])

column_handler =[0,3,6,9]

base_path = os.getcwd()
input_dirname = os.path.abspath(os.path.join(base_path,"..","..","input","visualize_lean_back"))
filenames = sorted(glob.glob(input_dirname + "/**/*.csv"))

for filename in filenames:
    basename = os.path.basename(filename)
    df_Kinect = pd.read_csv(filename)
    output_dirname = os.path.abspath(os.path.join(base_path,"..","..","output","visualize_lean_back"))
    out_folder = os.path.basename(os.path.abspath(os.path.join(filename,"..")))
    output_dirname = os.path.join(output_dirname,out_folder)
    os.makedirs(output_dirname,exist_ok=True)
    out_filename = os.path.join(output_dirname, basename.replace('.csv','_'+ column_header[column_handler[targ_column]]
    + '_' + seat_header[int(sys.argv[3])] +'_parsed_json.html'))
    title = "Plot"
    participant = os.path.basename(output_dirname)
    scatlayout_xt_yt = go.Layout(
        xaxis=dict(
            domain=[0, 1],
            title="Time",
            anchor="y2"
        ),
        yaxis1=dict(
            title="Skeleton Y",
            domain=[.52,1],
        ),
        yaxis2=dict(
            title="Skeleton Z",
            domain=[0,.48],
        ),
        title = title +" - "+ participant +" - Skeleton "+ column_header[column_handler[targ_column]] +" Joint vs Time",
    )
    scatfig_xyxt = plotly.graph_objs.Figure(layout=scatlayout_xt_yt)
    # xaxis = 'x1'
    # yaxis = 'y1'
    # targ_column = 3
    # # Kinect Look Point X vs t
    # xdata = df_Kinect["sensing_time"]
    # ydata = df_Kinect[columns_2[targ_column]]
    # trace_kinect = plotly.graph_objs.Scatter(
    #     x = xdata,y= ydata,xaxis=xaxis,yaxis=yaxis,
    #     name="Skeleton X",
    #     mode="markers",
    #     marker=dict(size=5, symbol="square"),
    #     )
    # scatfig_xyxt.add_trace(trace_kinect)

    xaxis = 'x1'
    yaxis = 'y1'
    # Kinect Look Point Y vs t
    xdata = df_Kinect["sensing_time"]
    if int(sys.argv[2]) == 0:
        ydata = df_Kinect[columns_2[targ_column+1]]
    elif int(sys.argv[2]) == 1:
        ydata = df_Kinect[columns_3[targ_column+1]]

    trace_kinect = plotly.graph_objs.Scatter(
        x = xdata,y= ydata,xaxis=xaxis,yaxis=yaxis,
        name="Skeleton Y",
        mode="markers",
        marker=dict(size=5, symbol="square"),
        )
    scatfig_xyxt.add_trace(trace_kinect)

    xaxis = 'x1'
    yaxis = 'y2'
    # Kinect Look Point Z vs t
    xdata = df_Kinect["sensing_time"]
    if int(sys.argv[2]) == 0:
        ydata = df_Kinect[columns_2[targ_column+1]]
    elif int(sys.argv[2]) == 1:
        ydata = df_Kinect[columns_3[targ_column+1]]

    trace_kinect = plotly.graph_objs.Scatter(
        x = xdata,y= ydata,xaxis=xaxis,yaxis=yaxis,
        name="Skeleton Z",
        mode="markers",
        marker=dict(size=5, symbol="square"),
        )
    scatfig_xyxt.add_trace(trace_kinect)


    plot_filepath = out_filename
    plotly.offline.plot(scatfig_xyxt, filename = plot_filepath,auto_open=auto_open)

print("Finished")
