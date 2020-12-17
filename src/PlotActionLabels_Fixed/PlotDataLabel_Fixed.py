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

print("S")
print("P")
print("A")
print("C")
print("E")

# Timestart = datetime.now()
# print("Start: " + str(Timestart))

cwd=os.getcwd()

###---
base_path = os.getcwd()
input_dirname = os.path.abspath(os.path.join(base_path,"..","..","input","PlotActionLabels_Fixed"))
filenames = sorted(glob.glob(input_dirname + "/*.csv"))
output_dirname = os.path.abspath(os.path.join(base_path,"..","..","output","PlotActionLabels_Fixed"))
out_folder = os.path.basename(os.path.abspath(os.path.join(filenames[0],"..")))
os.makedirs(output_dirname,exist_ok=True)

input_file = os.path.join(input_dirname,filenames[0])
csv_filepath = input_file
###---

output_path = os.path.join(output_dirname,"ActionLabel_FixedPlot.html")

title = "Action Labels"

# csv_filepath = os.path.join(cwd,"LabeledData","labeled_data","20201127_output_labeled_data","20201127_044256-20201127_045216_t202011_10hz_resampled_df_kinectTrial_1_-_Seat_2_-_Action_pt01_add_instructions_v2.csv")
# csv_filepath = os.path.join(cwd,"LabeledData","labeled_data","20201127_output_labeled_data","20201127_044256-20201127_045216_t202011_10hz_resampled_df_kinectTrial_1_-_Seat_3_-_Action_pt02_add_instructions_v2.csv")
# csv_filepath = os.path.join(cwd,"LabeledData","labeled_data","20201127_output_labeled_data","20201127_045506-20201127_050451_t202011_10hz_resampled_df_kinectTrial_2_-_Seat_2_-_Action_pt03_add_instructions_v2.csv")
# csv_filepath = os.path.join(cwd,"LabeledData","labeled_data","20201127_output_labeled_data","20201127_045506-20201127_050451_t202011_10hz_resampled_df_kinectTrial_2_-_Seat_3_-_Action_pt04_add_instructions_v2.csv")

df = pd.read_csv(csv_filepath)

# user_result_action_label_name
# attention 1
# looking_around 2
# other 4
# follow 3

action_label_number = np.zeros(len(df))

k=0
while (k<len(df)):
    if df['user_result_action_label_name'][k] == 'attention':
        action_label_number[k] = 1
    elif df['user_result_action_label_name'][k] == 'looking_around':
        action_label_number[k] = 2
    elif df['user_result_action_label_name'][k] == 'follow':
        action_label_number[k] = 3
    elif df['user_result_action_label_name'][k] == 'other':
        action_label_number[k] = 4

    k+=1

df['action_label_number'] = action_label_number

# print(df['action_label_number'].head())
scatlayout = go.Layout(
    xaxis=dict(
        domain=[0, 1],
        title="Sensing Time",
    ),
    yaxis=dict(
        title="Action Label",
        domain=[0, 1],
        ticktext=["attention", "looking_around", "follow","other"],
        tickvals=[1,2,3,4],
    ),
    title = title,
)
scatfig = plotly.graph_objs.Figure(layout=scatlayout)

xaxis = 'x1'
yaxis = 'y1'
# Kinect Look Point
xdata = df["sensing_time"]
ydata = df["action_label_number"]
trace_kinect = plotly.graph_objs.Scatter(
    x = xdata,y= ydata,xaxis=xaxis,yaxis=yaxis,
    name="Action Label",
    mode="markers",
    # marker=dict(size=3, symbol="line-ns",color="black"),
    marker=dict(symbol="line-ns-open",color="black",size=40),

    )
scatfig.add_trace(trace_kinect)


plot_filepath = os.path.join(cwd,title+"_Label_Fixed.html")
plotly.offline.plot(scatfig, filename = output_path,auto_open=True)
