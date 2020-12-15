# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from signal import signal, SIGINT
import time
import argparse

import os
stream = os.popen('mkdir bags && mkdir csvs')
output = stream.read()

#arg
parser = argparse.ArgumentParser(description='azure kinect dk calibration')
parser.add_argument('--camera_no', type=int, default=0) # カメラ番号
parser.add_argument('--mode', type=int, default=0) # モード 0:プレビューなし, 1:プレビューあり, 2:顔キャプチャモード
parser.add_argument('--save_capture', type=int, default=0) # プレビュー時保存フラグ
args = parser.parse_args()

running_procs = [
    #Popen("python3 ~/share/work/20200907/toyota_boshoku/src/main_azure_kinect_action_dk.py", shell=True),
    #Popen("cd bags && ros2 bag record -a -o all_topic", shell=True),
    Popen("cd bags && ros2 bag record  \
    /moox/data/sensor/detect_action/c_2 \
    /moox/data/sensor/detect_action/c_3 \
    /moox/data/sensor/azure_kinect/c_0 \
    /moox/data/sensor/azure_kinect/c_98 \
    /moox/data/sensor/azure_kinect/c_99 \
    /moox/data/sensor/sitting_seat -o kinect_topics", shell=True),

    #Popen("cd csvs && ros2 topic echo -f --csv /moox/data/sensor/azure_kinect/c_0 > kinect_c0.csv", shell=True),
    #Popen("cd csvs && ros2 topic echo -f --csv /moox/data/sensor/detect_action/c_1 > action_c1.csv", shell=True),
    Popen("cd csvs && ros2 topic echo -f --csv /moox/data/sensor/detect_action/c_2 > action_c2.csv", shell=True),
    Popen("cd csvs && ros2 topic echo -f --csv /moox/data/sensor/detect_action/c_3 > action_c3.csv", shell=True),
    Popen("cd csvs && ros2 topic echo -f --csv /moox/data/sensor/azure_kinect/c_98 > kinect_c98.csv", shell=True),
    Popen("cd csvs && ros2 topic echo -f --csv /moox/data/sensor/azure_kinect/c_99 > kinect_c99.csv", shell=True),
    Popen("cd csvs && ros2 topic echo -f --csv /moox/data/sensor/sitting_seat > sitting_seat.csv", shell=True),

    #Popen(['ros2', 'run', 'moox_detect_gesture', 'run', '--no', '1'], bufsize=0),
    #Popen(['ros2', 'run', 'moox_detect_gesture', 'run', '--no', '2'], bufsize=0),
    #Popen(['ros2', 'run', 'moox_detect_gesture', 'run', '--no', '3'], bufsize=0),

    #Popen(['ros2', 'run', 'moox_detect_section', 'run', '--no', '1'], bufsize=0),
    #Popen(['ros2', 'run', 'moox_detect_section', 'run', '--no', '2'], bufsize=0),
    #Popen(['ros2', 'run', 'moox_detect_section', 'run', '--no', '3'], bufsize=0),

    #Popen(['python3', './upload/upload_data.py'], bufsize=0),
    #Popen(['ros2', 'run', 'moox_sensor_data', 'publisher'], bufsize=0),
    #Popen(['./azure_kinect_dk/body_tracking', str(args.camera_no), str(args.mode), str(args.save_capture)], bufsize=0),
    #Popen(['./azure_kinect_dk/body_tracking', str(0), str(0), str(0)], bufsize=0),
    #Popen(['./azure_kinect_dk/body_tracking', str(1), str(0), str(0)], bufsize=0),
    ]

for proc in running_procs:
    proc.poll()

try:
    while True:
        time.sleep(.1)
except KeyboardInterrupt:
    for proc in running_procs:
        proc.send_signal(SIGINT)
        proc.communicate()
        proc.terminate()
