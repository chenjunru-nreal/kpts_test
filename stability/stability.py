#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 19:11:10 2022

@author: zhengyi
"""








pd_index_list.append("average(max for pk_pk)")

pd_data["x_mean"].append(np.mean(pd_data["x_mean"]))
pd_data["x_std"].append(np.mean(pd_data["x_std"]))
pd_data["x_abs_mean_err"].append(np.mean(pd_data["x_abs_mean_err"]))
pd_data["y_mean"].append(np.mean(pd_data["y_mean"]))
pd_data["y_std"].append(np.mean(pd_data["y_std"]))
pd_data["y_abs_mean_err"].append(np.mean(pd_data["y_abs_mean_err"]))
pd_data["z_mean"].append(np.mean(pd_data["z_mean"]))
pd_data["z_std"].append(np.mean(pd_data["z_std"]))
pd_data["z_abs_mean_err"].append(np.mean(pd_data["z_abs_mean_err"]))
pd_data["space_abs_mean_err"].append(np.mean(pd_data["space_abs_mean_err"]))
pd_data["pk_pk_x"].append(np.max(pd_data["pk_pk_x"]))
pd_data["pk_pk_y"].append(np.max(pd_data["pk_pk_y"]))
pd_data["pk_pk_z"].append(np.max(pd_data["pk_pk_z"]))
pd_data["pk_pk_angle_x"].append(np.max(pd_data["pk_pk_angle_x"]))
pd_data["pk_pk_angle_y"].append(np.max(pd_data["pk_pk_angle_y"]))
pd_data["pk_pk_angle_z"].append(np.max(pd_data["pk_pk_angle_z"]))


df = pd.DataFrame(pd_data, index = pd_index_list)
df.to_excel('analysis_report.xls',sheet_name='data_report')




