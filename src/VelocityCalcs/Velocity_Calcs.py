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
input_dirname = os.path.abspath(os.path.join(base_path,"..","..","input","VelocityCalcs"))
filenames = sorted(glob.glob(input_dirname + "/*.csv"))
output_dirname = os.path.abspath(os.path.join(base_path,"..","..","output","VelocityCalcs"))
out_folder = os.path.basename(os.path.abspath(os.path.join(filenames[0],"..")))
os.makedirs(output_dirname,exist_ok=True)

input_file = os.path.join(input_dirname,filenames[0])
csv_filepath = input_file
df = pd.read_csv(csv_filepath)
###---

output_path = os.path.join(output_dirname,"Velocities.csv")

# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 2 - Seat 3 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 2 - Seat 2 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 1 - Seat 3 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 1 - Seat 2 - Action.csv")
df = pd.read_csv(csv_filepath)

# outpath = os.path.join(cwd,"df_Velocity","df_Vel_kinectTrial 2 - Seat 3 - Action.csv")
# outpath = os.path.join(cwd,"df_Velocity","df_Vel_kinectTrial 2 - Seat 2 - Action.csv")
# outpath = os.path.join(cwd,"df_Velocity","df_Vel_kinectTrial 1 - Seat 3 - Action.csv")
# outpath = os.path.join(cwd,"df_Velocity","df_Vel_kinectTrial 1 - Seat 2 - Action.csv")
outpath = output_path
#Velocity columns
#neck, head, R_eye, L_eye, nose, R_ear, L_ear, face_direction_horizontal, face_direction_vertical
# data_body_raw_neck_x
# data_body_raw_head_x
# data_body_raw_nose_x
# data_body_raw_l_eyes_x
# data_body_raw_r_eyes_x
# data_body_raw_l_ear_x
# data_body_raw_r_ear_x
# Sum of velocities
# data_status_face_direction_face_direction_horizontal
# data_status_face_direction_face_direction_vertical
# maybe pythagorize face direction

vel_Head = np.empty(len(df))
vel_Head[:] = np.NaN
vel_Neck = np.empty(len(df))
vel_Neck[:] = np.NaN
vel_Nose = np.empty(len(df))
vel_Nose[:] = np.NaN
vel_Leye = np.empty(len(df))
vel_Leye[:] = np.NaN
vel_Reye = np.empty(len(df))
vel_Reye[:] = np.NaN
vel_Lear = np.empty(len(df))
vel_Lear[:] = np.NaN
vel_Rear = np.empty(len(df))
vel_Rear[:] = np.NaN
vel_Sum_Joints = np.empty(len(df))
vel_Sum_Joints[:] = np.NaN
vel_Hfacedir = np.empty(len(df))
vel_Hfacedir[:] = np.NaN
vel_Vfacedir = np.empty(len(df))
vel_Vfacedir[:] = np.NaN
vel_FaceDir_combined = np.empty(len(df))
vel_FaceDir_combined[:] = np.NaN
###############################################
vel_Head_mov10 = np.empty(len(df))
vel_Head_mov10[:] = np.NaN
vel_Neck_mov10 = np.empty(len(df))
vel_Neck_mov10[:] = np.NaN
vel_Nose_mov10 = np.empty(len(df))
vel_Nose_mov10[:] = np.NaN
vel_Leye_mov10 = np.empty(len(df))
vel_Leye_mov10[:] = np.NaN
vel_Reye_mov10 = np.empty(len(df))
vel_Reye_mov10[:] = np.NaN
vel_Lear_mov10 = np.empty(len(df))
vel_Lear_mov10[:] = np.NaN
vel_Rear_mov10 = np.empty(len(df))
vel_Rear_mov10[:] = np.NaN
vel_Sum_Joints_mov10 = np.empty(len(df))
vel_Sum_Joints_mov10[:] = np.NaN
vel_Hfacedir_mov10 = np.empty(len(df))
vel_Hfacedir_mov10[:] = np.NaN
vel_Vfacedir_mov10 = np.empty(len(df))
vel_Vfacedir_mov10[:] = np.NaN
vel_FaceDir_combined_mov10 = np.empty(len(df))
vel_FaceDir_combined_mov10[:] = np.NaN


# vel_Head,vel_Nose,vel_Leye,vel_Reye,vel_Lear,vel_Rear = vel_Neck,vel_Neck,vel_Neck,vel_Neck,vel_Neck,vel_Neck
# vel_Sum_Joints,vel_Hfacedir,vel_Vfacedir,vel_FaceDir_combined = vel_Neck,vel_Neck,vel_Neck,vel_Neck

# print(vel_Head)

k=0
while (k<len(df)-1):
    vel_Neck[k] = ((df['data_body_raw_neck_x'][k]-df['data_body_raw_neck_x'][k+1])**2+(df['data_body_raw_neck_y'][k]-df['data_body_raw_neck_y'][k+1])**2+(df['data_body_raw_neck_z'][k]-df['data_body_raw_neck_z'][k+1])**2)**0.5
    vel_Head[k] = ((df['data_body_raw_head_x'][k]-df['data_body_raw_head_x'][k+1])**2+(df['data_body_raw_head_y'][k]-df['data_body_raw_head_y'][k+1])**2+(df['data_body_raw_head_z'][k]-df['data_body_raw_head_z'][k+1])**2)**0.5
    vel_Nose[k] = ((df['data_body_raw_nose_x'][k]-df['data_body_raw_nose_x'][k+1])**2+(df['data_body_raw_nose_y'][k]-df['data_body_raw_nose_y'][k+1])**2+(df['data_body_raw_nose_z'][k]-df['data_body_raw_nose_z'][k+1])**2)**0.5
    vel_Leye[k] = ((df['data_body_raw_l_eyes_x'][k]-df['data_body_raw_l_eyes_x'][k+1])**2+(df['data_body_raw_l_eyes_y'][k]-df['data_body_raw_l_eyes_y'][k+1])**2+(df['data_body_raw_l_eyes_z'][k]-df['data_body_raw_l_eyes_z'][k+1])**2)**0.5
    vel_Reye[k] = ((df['data_body_raw_r_eyes_x'][k]-df['data_body_raw_r_eyes_x'][k+1])**2+(df['data_body_raw_r_eyes_y'][k]-df['data_body_raw_r_eyes_y'][k+1])**2+(df['data_body_raw_r_eyes_z'][k]-df['data_body_raw_r_eyes_z'][k+1])**2)**0.5
    vel_Lear[k] = ((df['data_body_raw_l_ear_x'][k]-df['data_body_raw_l_ear_x'][k+1])**2+(df['data_body_raw_l_ear_y'][k]-df['data_body_raw_l_ear_y'][k+1])**2+(df['data_body_raw_l_ear_z'][k]-df['data_body_raw_l_ear_z'][k+1])**2)**0.5
    vel_Rear[k] = ((df['data_body_raw_r_ear_x'][k]-df['data_body_raw_r_ear_x'][k+1])**2+(df['data_body_raw_r_ear_y'][k]-df['data_body_raw_r_ear_y'][k+1])**2+(df['data_body_raw_r_ear_z'][k]-df['data_body_raw_r_ear_z'][k+1])**2)**0.5

    vel_Sum_Joints[k] = (vel_Neck[k]+vel_Head[k]+vel_Nose[k]+vel_Leye[k]+vel_Reye[k]+vel_Lear[k]+vel_Rear[k])

    vel_Hfacedir[k] = abs(df['data_status_face_direction_face_direction_horizontal'][k]-df['data_status_face_direction_face_direction_horizontal'][k+1])
    vel_Vfacedir[k] = abs(df['data_status_face_direction_face_direction_vertical'][k]-df['data_status_face_direction_face_direction_vertical'][k+1])

    vel_FaceDir_combined[k] = (vel_Hfacedir[k]**2 + vel_Vfacedir[k]**2)**0.5

    #Moving Averages
    if k > 10: #moving average 10
        # print("hi")
        vel_Head_mov10[k] = sum(vel_Head[k-10:k])/10
        vel_Neck_mov10[k] = sum(vel_Neck[k-10:k])/10
        vel_Nose_mov10[k] = sum(vel_Nose[k-10:k])/10
        vel_Leye_mov10[k] = sum(vel_Leye[k-10:k])/10
        vel_Reye_mov10[k] = sum(vel_Reye[k-10:k])/10
        vel_Lear_mov10[k] = sum(vel_Lear[k-10:k])/10
        vel_Rear_mov10[k] = sum(vel_Rear[k-10:k])/10
        vel_Sum_Joints_mov10[k] = sum(vel_Sum_Joints[k-10:k])/10
        vel_Hfacedir_mov10[k] = sum(vel_Hfacedir[k-10:k])/10
        vel_Vfacedir_mov10[k] = sum(vel_Vfacedir[k-10:k])/10
        vel_FaceDir_combined_mov10[k] = sum(vel_FaceDir_combined[k-10:k])/10


    k+=1
# print(vel_Neck)

df['vel_Neck'] = vel_Neck
df['vel_Head'] = vel_Head
df['vel_Nose'] = vel_Nose
df['vel_Leye'] = vel_Leye
df['vel_Reye'] = vel_Reye
df['vel_Lear'] = vel_Lear
df['vel_Rear'] = vel_Rear
df['vel_Sum_Joints'] = vel_Sum_Joints
df['vel_Hfacedir'] = vel_Hfacedir
df['vel_Vfacedir'] = vel_Vfacedir
df['vel_FaceDir_combined'] = vel_FaceDir_combined

df['vel_Neck_mov10'] = vel_Neck_mov10
df['vel_Head_mov10'] = vel_Head_mov10
df['vel_Nose_mov10'] = vel_Nose_mov10
df['vel_Leye_mov10'] = vel_Leye_mov10
df['vel_Reye_mov10'] = vel_Reye_mov10
df['vel_Lear_mov10'] = vel_Lear_mov10
df['vel_Rear_mov10'] = vel_Rear_mov10
df['vel_Sum_Joints_mov10'] = vel_Sum_Joints_mov10
df['vel_Hfacedir_mov10'] = vel_Hfacedir_mov10
df['vel_Vfacedir_mov10'] = vel_Vfacedir_mov10
df['vel_FaceDir_combined_mov10'] = vel_FaceDir_combined_mov10


df.to_csv(outpath)

Timeend = datetime.now()
TimeTaken = Timeend - Timestart
print("Time: " + str(TimeTaken) + " seconds")

print("DONE")
