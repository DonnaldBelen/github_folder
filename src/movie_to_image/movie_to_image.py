import cv2
import os
from os.path import splitext, dirname, basename, join
from os import path
import glob

def save_frames(video_path: str, frame_dir: str, name="image", ext="jpg"):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return
    v_name = splitext(basename(video_path))[0]
    if frame_dir[-1:] == "\\" or frame_dir[-1:] == "/":
        frame_dir = dirname(frame_dir)
    frame_dir_ = join(frame_dir, v_name)

    os.makedirs(frame_dir_, exist_ok=True)
    base_path = join(frame_dir_, name)

    idx = 0
    while cap.isOpened():
        idx += 0.1
        ret, frame = cap.read()
        if ret:
            if cap.get(cv2.CAP_PROP_POS_FRAMES) == 1:  # 0秒のフレームを保存
                cv2.imwrite("{}_{}.{}".format(base_path, "0000", ext),
                            frame)
            elif idx < cap.get(cv2.CAP_PROP_FPS):
                continue
            else:  # 1秒ずつフレームを保存
                second = int(cap.get(cv2.CAP_PROP_POS_FRAMES)/idx)
                filled_second = str(second).zfill(4)
                cv2.imwrite("{}_{}.{}".format(base_path, filled_second, ext),
                            frame)
                idx = 0
        else:
            break

base_path = os.getcwd()
input_dir = path.abspath(path.join(base_path,"..","..","input","movie_to_image"))
output = path.abspath(path.join(base_path,"..","..","output","movie_to_image"))
final_dir = glob.glob(input_dir + "/*.mp4")

save_frames(final_dir,output)