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

from datetime import datetime #Just to track the amount of time it takes to plot

Timestart = datetime.now()
print("Start: " + str(Timestart))


# print("START")

cwd=os.getcwd()


#Deal with standard file structure
input_filepath = os.path.join(cwd,'..','input')
input_filenames = os.listdir(input_filepath)
# print(input_filenames)
input_file = os.path.join(input_filepath,input_filenames[0]) #for now can only use 1 file at a time
csv_filepath = input_file

output_path = os.path.join(cwd,'..','output',"Animated_Gaze_XY.mp4")
# output_path_y = os.path.join(cwd,'..','output',"Animated_GazeY.mp4")
###

# title = "Trial 1 - Seat 2"

# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 2 - Seat 3 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 2 - Seat 2 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 1 - Seat 3 - Action.csv")
# csv_filepath = os.path.join(cwd,"df_Kinect","df_kinectTrial 1 - Seat 2 - Action.csv")
df = pd.read_csv(csv_filepath)

df = df.reset_index()
df['times']=df['index']*(0.1) #Technically lazy way because I know its 0.1s increments
tvals = df['times'] #time values
xvals = df['data_fast_status_look_points_look_point_center_x']
yvals = df['data_fast_status_look_points_look_point_center_y']

# Mock Data Block Start
# csv_filepath = os.path.join(cwd,"MockAnimateData.csv")
# df = pd.read_csv(csv_filepath)
# tvals = df['sensing_time']
# xvals = df['ValsX']
# yvals = df['ValsY']
# print(tdata)
# Mock Data Block End

Writer = animation.writers['ffmpeg']
writer = Writer(fps=10, bitrate=1800)

fig = plt.figure(figsize=(18, 9)) #idk the units
# fig = plt.figure()
# fig.title('test title', fontsize=20)

# Gridlines
# fig.grid(b=True, which='major', color='#666666', linestyle='-')
# fig.minorticks_on()
# fig.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
# ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
# ax = plt.axes(xlim=(0,10), ylim=(-10,10))
# ax = plt.axes(xlim=(tvals.min()-1,tvals.max()+1), ylim=(xvals.min()-1,xvals.max()+1))
# ax = plt.axes(ylim=(yvals.min()-1,yvals.max()+1), xlim=(xvals.min()-1,xvals.max()+1))
ax = plt.axes(xlim=(-1501,1501), ylim=(-1001,1001))
line, = ax.plot([], [],'o-', lw=2,)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.xticks(np.arange(-1500, 1500, 100.0))
plt.yticks(np.arange(-1000, 1000, 100.0))
plt.title('Kinect Gaze X vs Gaze Y', fontsize=18)
plt.xlabel('Gaze X', fontsize=18)
plt.ylabel('Gaze Y', fontsize=16)

time_text = ax.text(0.8, 1.02, '', transform=ax.transAxes, fontsize=14, bbox=dict(facecolor='white')) #make a textbox to show sensing time


# initialization function
def init():
	# creating an empty plot/frame
	line.set_data([], [])
	time_text.set_text('')
	return line,time_text #adding text here is what makes it so it can update per frame

xdata, ydata = [], []
xxdata = []
yydata = []
xint=[]
yint=[]

def animate(i):
	# t is a parameter
	t = i

	# x, y values to be plotted
	x = xvals[i]
	y = yvals[i]

	# appending new points to x, y axes points list
	xdata.append(x)
	ydata.append(y)

	if i >21:
		xxdata = xdata[i-20:i]
		yydata = ydata[i-20:i]
	else:
		xxdata = xdata
		yydata = ydata


	# ax.set_xlim((t-100)/10,(t+20)/10) #This slides the X-axis

	# textstr = i

	print(i)

	line.set_data(xxdata, yydata)
	# time_text.set_text(time_template % (i*dt))
	# time_text.set_text(t*0.1)

	time_text.set_text(df['sensing_time'][i])
	return line,time_text

# plt.axis('off')
# plt.style.use('dark_background')
# anim = animation.FuncAnimation(fig, animate, init_func=init,
# 							frames=len(tvals)-1, interval=20, blit=True) #interval is delay between frames

anim = animation.FuncAnimation(fig, animate, init_func=init,
							frames=len(tvals)-1, interval=20, blit=True) #interval is delay between frames
# anim = animation.FuncAnimation(fig, animate, init_func=init,
# 							frames=100, interval=20, blit=True) #interval is delay between frames

anim.save(output_path,writer=writer)

Timeend = datetime.now()

TimeTaken = Timeend - Timestart
print("Time: " + str(TimeTaken) + " seconds")

print("DONE")
