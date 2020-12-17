# Trying to Animate the kinect plots

import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly
import datetime
import matplotlib
import matplotlib.pyplot as plt

import matplotlib.animation as animation

print("START")

cwd=os.getcwd()

#Deal with standard file structure
input_filepath = os.path.join(cwd,'..','input')
input_filenames = os.listdir(input_filepath)
# print(input_filenames)
input_file = os.path.join(input_filepath,input_filenames[0]) #for now can only use 1 file at a time
csv_filepath = input_file

output_path_x = os.path.join(cwd,'..','output',"Animated_GazeX.mp4")
output_path_y = os.path.join(cwd,'..','output',"Animated_GazeY.mp4")


title = "Trial 1 - Seat 2"

# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 2 - Seat 3 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 2 - Seat 2 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 1 - Seat 3 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 1 - Seat 2 - Action.csv")
df = pd.read_csv(csv_filepath)

df = df.reset_index()
df['times']=df['index']*(0.1) #Technically lazy way because I know its 0.1s increments
tvals = df['times'] #time values
# tvals = df['sensing_time']
xvals = df['data_fast_status_look_points_look_point_center_x']
yvals = df['data_fast_status_look_points_look_point_center_y']

Writer = animation.writers['ffmpeg']
writer = Writer(fps=10, bitrate=1800)

fig = plt.figure(figsize=(18, 9)) #idk the units

ax = plt.axes(xlim=(0,10), ylim=(xvals.min()-1,xvals.max()+1))
line, = ax.plot([], [],'o-', lw=2)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.xticks(np.arange(0, len(df), 1.0)) #Changes ticks to 1 apart - Major performance hit for some reason
plt.title('Kinect Gaze X over Time', fontsize=18)
plt.xlabel('Sensing Time from Start (s)', fontsize=18)
plt.ylabel('Gaze X', fontsize=16)

time_text = ax.text(0.8, 1.02, '', transform=ax.transAxes, fontsize=14,bbox=dict(facecolor='white')) #make a textbox to show sensing time

# initialization function
def init():
	# creating an empty plot/frame
	line.set_data([], [])
	time_text.set_text('')

	return line,time_text

xdata, ydata = [], []
xint=[]
yint=[]

def animateX(i):
	# t is a parameter
	t = i

	print(i)

	# x, y values to be plotted
	x = tvals[i]
	y = xvals[i]

	# appending new points to x, y axes points list
	xdata.append(x)
	ydata.append(y)

	ax.set_xlim((t-100)/10,(t+20)/10) #This slides the X-axis
	time_text.set_text(df['sensing_time'][i])

	line.set_data(xdata, ydata)
	return line,

anim = animation.FuncAnimation(fig, animateX, init_func=init,
							frames=len(tvals)-1, interval=20, blit=True) #interval is delay between frames

# anim = animation.FuncAnimation(fig, animateX, init_func=init,
# 							frames=300, interval=20, blit=True)

anim.save(output_path_x,writer=writer)

################ Y ###################################

plt.title('Kinect Gaze Y over Time', fontsize=18)
plt.xlabel('Sensing Time from Start (s)', fontsize=18)
plt.ylabel('Gaze Y', fontsize=16)
# initialization function
def init():
	# creating an empty plot/frame
	line.set_data([], [])
	time_text.set_text('')

	return line,time_text

xdata, ydata = [], []
xint=[]
yint=[]

def animateY(i):
	# t is a parameter
	t = i

	print(i)

	# x, y values to be plotted
	x = tvals[i]
	y = yvals[i]

	# appending new points to x, y axes points list
	xdata.append(x)
	ydata.append(y)

	ax.set_xlim((t-100)/10,(t+20)/10) #This slides the X-axis
	time_text.set_text(df['sensing_time'][i])

	line.set_data(xdata, ydata)
	return line,

anim = animation.FuncAnimation(fig, animateY, init_func=init,
							frames=len(tvals)-1, interval=20, blit=True) #interval is delay between frames

# anim = animation.FuncAnimation(fig, animateY, init_func=init,
# 							frames=300, interval=20, blit=True)

anim.save(output_path_y,writer=writer)

print("DONE")
