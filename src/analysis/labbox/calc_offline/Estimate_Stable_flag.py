# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


class Estimate_Stable_flag:
    def __init__(self, sum_window=4, col_window=10, threshold=0.1):
        self.version = 'TM20201203'
        self.sum_window = sum_window
        self.col_window = col_window
        self.threshold = threshold

    def calc_face_dir_ward_flag(self, df, col_in, col_out):
        # 差分方向の量子化
        # col_in = 'data_status_face_direction_face_direction_horizontal'
        # col_out = "face_dir_ward_flag_horizontal"
        df[col_out] = df[col_in]
        # 差分の量子化(増減に変換)
        df[col_out] = df[col_out].diff(1)
        df.loc[(df[col_out] < 0), col_out] = -1
        df.loc[(df[col_out] > 0), col_out] = 1
        df.loc[(df[col_out] == 0), col_out] = 0
        return df

    def calc_moving_stable_flag(self, df, col_in, col_out, sum_window):
        # Moving/Stable フラグ化
        # col_in = 'face_dir_ward_flag_horizontal'
        # col_out = "face_dir_ms_flag_horizontal"
        # sum_window = 4  # 偶数のみ指定可
        df[col_out] = df[col_in]
        # ある程度の範囲で積算(偶数のみ)
        df[col_out] = df[col_out].rolling(sum_window, center=True).sum()
        df[col_out] = np.abs(df[col_out])
        # フラグ化
        df.loc[~(df[col_out] == 0), col_out] = -99
        df.loc[(df[col_out] == 0), col_out] = 1
        df.loc[(df[col_out] == -99), col_out] = 0
        return df

    def calc_interest_flag_from_face_ward(self, df, col_in, col_out, col_window, threshold):
        # 集約化
        # col_in = "face_dir_ms_flag_horizontal"
        # col_out = "face_dir_interest_flag_horizontal"
        # col_window1 = 10
        # threshold1 = 0.1
        df[col_out] = df[col_in].rolling(col_window, center=True).mean()
        df.loc[~(df[col_out] > threshold), col_out] = 0
        df.loc[(df[col_out] > threshold), col_out] = 1
        return df

    def run(self, df, col_in, col_out, is_test):
        # セット
        all_col_in = col_in
        all_col_out = col_out
        # 差分方向の量子化
        # col_in = 'data_status_face_direction_face_direction_horizontal'
        col_in = all_col_in
        col_out = "face_dir_ward_flag_horizontal"
        df = self.calc_face_dir_ward_flag(df, col_in, col_out)
        # Moving/Stable フラグ化
        col_in = 'face_dir_ward_flag_horizontal'
        col_out = "face_dir_ms_flag_horizontal"
        sum_window = 4  # 偶数のみ指定可
        df = self.calc_moving_stable_flag(df, col_in, col_out, sum_window)
        # 集約化
        col_in = "face_dir_ms_flag_horizontal"
        # col_out = "face_dir_interest_flag_horizontal"
        col_out = all_col_out
        col_window = self.col_window
        threshold = self.threshold
        df = self.calc_interest_flag_from_face_ward(
            df, col_in, col_out, col_window, threshold)
        # 途中項の削除
        if not (is_test):
            col_temp_1 = "face_dir_ward_flag_horizontal"
            df = df.drop(columns=col_temp_1)
            col_temp_2 = "face_dir_ms_flag_horizontal"
            df = df.drop(columns=col_temp_2)
        return df
