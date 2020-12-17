import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly
import datetime
import matplotlib
import matplotlib.pyplot as plt
import math

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

#Deal with standard file structure
input_filepath = os.path.join(cwd,'..','input')
input_filenames = os.listdir(input_filepath)
# print(input_filenames)
input_file = os.path.join(input_filepath,input_filenames[0]) #for now can only use 1 file at a time
csv_filepath = input_file

output_path = os.path.join(cwd,'..','output',"ActionLabel_AnimatedPlot.mp4")

title = "Trial 1 Seat 3 - Labeled Data - Animated"

# csv_filepath = os.path.join(cwd,"LabeledData","labeled_data","20201127_output_labeled_data","20201127_044256-20201127_045216_t202011_10hz_resampled_df_kinectTrial_1_-_Seat_2_-_Action_pt01_add_instructions_v2.csv")
# csv_filepath = os.path.join(cwd,"LabeledData","labeled_data","20201127_output_labeled_data","20201127_044256-20201127_045216_t202011_10hz_resampled_df_kinectTrial_1_-_Seat_3_-_Action_pt02_add_instructions_v2.csv")
# csv_filepath = os.path.join(cwd,"LabeledData","labeled_data","20201127_output_labeled_data","20201127_045506-20201127_050451_t202011_10hz_resampled_df_kinectTrial_2_-_Seat_2_-_Action_pt03_add_instructions_v2.csv")
# csv_filepath = os.path.join(cwd,"LabeledData","labeled_data","20201127_output_labeled_data","20201127_045506-20201127_050451_t202011_10hz_resampled_df_kinectTrial_2_-_Seat_3_-_Action_pt04_add_instructions_v2.csv")

df = pd.read_csv(csv_filepath)

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

df = df.reset_index()
df['times']=df['index']*(0.1) #Technically lazy way because I know its 0.1s increments
tvals = df['times'] #time values
yvals = df['action_label_number']

Writer = animation.writers['ffmpeg']
writer = Writer(fps=10, bitrate=1800)

fig = plt.figure(figsize=(18, 9)) #idk the units

ax = plt.axes(xlim=(0,10), ylim=(0.5,4.5))
line, = ax.plot([], [],'o-', lw=2)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.xticks(np.arange(0, len(df), 1.0)) #Changes ticks to 1 apart - Major performance hit for some reason
plt.title('Action Label over Time', fontsize=18)
plt.xlabel('Sensing Time from Start (s)', fontsize=18)
plt.ylabel('Action Label', fontsize=16)

plt.yticks([1,2,3,4],['attention','looking_around','follow','other']) #Changes ticks to 1 apart - Major performance hit for some reason

time_text = ax.text(0.8, 1.02, '', transform=ax.transAxes, fontsize=14,bbox=dict(facecolor='white')) #make a textbox to show sensing time
action_label_text = ax.text(0.0, 1.05, '', transform=ax.transAxes, fontsize=18,bbox=dict(facecolor='wheat'))

# initialization function
def init():
	# creating an empty plot/frame
	line.set_data([], [])
	time_text.set_text('')
	action_label_text.set_text('')


	return line,time_text,action_label_text,

xdata, ydata = [], []
xint=[]
yint=[]

def animate(i):
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

    #This line must be comma (,) - It cannot be on separate lines
	time_text.set_text(df['sensing_time'][i]),action_label_text.set_text(df['user_result_action_label_name'][i])


	line.set_data(xdata, ydata)
	return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
							frames=len(tvals)-1, interval=20, blit=True) #interval is delay between frames

# anim = animation.FuncAnimation(fig, animate, init_func=init,
# 							frames=300, interval=20, blit=True)

anim.save(output_path,writer=writer)



print("Done")
