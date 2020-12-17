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
input_dirname = os.path.abspath(os.path.join(base_path,"..","..","input","AngularVelocityCalcs"))
filenames = sorted(glob.glob(input_dirname + "/*.csv"))
output_dirname = os.path.abspath(os.path.join(base_path,"..","..","output","AngularVelocityCalcs"))
out_folder = os.path.basename(os.path.abspath(os.path.join(filenames[0],"..")))
os.makedirs(output_dirname,exist_ok=True)
###---
input_file = os.path.join(input_dirname,filenames[0])
csv_filepath = input_file

output_path = os.path.join(output_dirname,"AngularVelocities.csv")

# title = "Trial 2 - Seat 3"

# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 2 - Seat 3 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 2 - Seat 2 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 1 - Seat 3 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 1 - Seat 2 - Action.csv")
csv_filepath = input_file
df = pd.read_csv(csv_filepath)

# outpath = os.path.join(cwd,"df_AngularVelocity","df_AngVel_kinectTrial 2 - Seat 3 - Action.csv")
# outpath = os.path.join(cwd,"df_AngularVelocity","df_AngVel_kinectTrial 2 - Seat 2 - Action.csv")
# outpath = os.path.join(cwd,"df_AngularVelocity","df_AngVel_kinectTrial 1 - Seat 3 - Action.csv")
outpath = os.path.join(cwd,"df_AngularVelocity","df_AngVel_kinectTrial 1 - Seat 2 - Action.csv")
outpath = output_path

df = df.reset_index()
df['times']=df['index']*(0.1) #Technically lazy way because I know its 0.1s increments
tvals = df['sensing_time'] #time values
xvals = df['data_fast_status_look_points_look_point_center_x']
yvals = df['data_fast_status_look_points_look_point_center_y']

# Constants
MovingAvg_size = 10
MovingAvg_size_50 = 50


#The new vars
d01=0.0
d02=0.0
d12=0.0
gaze_theta=0.0
gaze_omega=0.0

omega_array=np.zeros(len(df))
MovingAvg_omega=np.zeros(len(df))
MovingAvg50_omega=np.zeros(len(df))

# df["gaze_omega"] =
#We'll use noze as origin
k=0
while (k<len(df)-1):
    # print("hi")data_body_raw_nose_x
    x0 = df['data_body_raw_nose_x'][k]
    y0 = df['data_body_raw_nose_y'][k]
    z0 = df['data_body_raw_nose_z'][k]
    x1 = df['data_fast_status_look_points_look_point_center_x'][k]
    y1 = df['data_fast_status_look_points_look_point_center_y'][k]
    z1 = df['data_fast_status_look_points_look_point_center_z'][k]
    x2 = df['data_fast_status_look_points_look_point_center_x'][k+1]
    y2 = df['data_fast_status_look_points_look_point_center_y'][k+1]
    z2 = df['data_fast_status_look_points_look_point_center_z'][k+1]
    t0 = df['times'][k]
    t1 = df['times'][k+1]

    d01 = (((x0-x1)**2)+((y0-y1)**2)+((z0-z1)**2))**0.5
    d02 = (((x0-x2)**2)+((y0-y2)**2)+((z0-z2)**2))**0.5
    d12 = (((x1-x2)**2)+((y1-y2)**2)+((z1-z2)**2))**0.5

    inter_top = ((d01**2) + (d02**2) - (d12**2)) #Just intermediate numbers in the formula to make it look cleaner
    inter_bot = 2*d01*d02
    gaze_theta = math.acos((inter_top/inter_bot)) #RuntimeWarning: invalid value encountered in double_scalars - I think it gives a few divide by 0, should be okay
    gaze_omega = gaze_theta / (t1-t0)

    # df.at["data_fast_status_look_points_look_point_center_z",k] = gaze_omega
    # omega_array = np.append(omega_array,gaze_omega)
    omega_array[k] = gaze_omega

    #Moving Averages
    if k > MovingAvg_size:
        MovingAvg_omega[k] = sum(omega_array[k-MovingAvg_size:k])/MovingAvg_size
    if k > MovingAvg_size_50:
        MovingAvg50_omega[k] = sum(omega_array[k-MovingAvg_size_50:k])/MovingAvg_size_50

    # print(k)
    k+=1

# print(df['data_fast_status_look_points_look_point_center_x'][2])
# print(omega_array)
df["omega_array"] = omega_array #I think rad/s
df["omega_deg"] = df["omega_array"]*(180/(math.pi))
# print(df["omega_array"].head())
# print(df["omega_deg"].head())

df["MovingAvg_omega"] = MovingAvg_omega
# print(df["MovingAvg_omega"].tail())
df["MovingAvg_omega_deg"] = df["MovingAvg_omega"]*(180/(math.pi))

df["MovingAvg50_omega"] = MovingAvg50_omega
# print(df["MovingAvg50_omega"].tail())
df["MovingAvg50_omega_deg"] = df["MovingAvg50_omega"]*(180/(math.pi))


df.to_csv(outpath)


Timeend = datetime.now()
TimeTaken = Timeend - Timestart
print("Time: " + str(TimeTaken) + " seconds")

# print(MovingAvg_omega)

print("DONE")
