## numpy is used for creating fake data
import numpy as np
import matplotlib as mpl
import pandas as pd
## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt

DataUrl = "C:/HR_Data.xlsx"
histUrl="histograms/"

df = pd.read_excel(DataUrl,"Worksheet",parse_cols=8)
df["satisfaction_level"].plot.hist()
fig = plt.figure(1, figsize=(20, 100))
fig.savefig(histUrl+'hist_satisfaction_level.png', bbox_inches='tight')
plt.close(fig)

df = pd.read_excel(DataUrl,"Worksheet",parse_cols=8)
df["last_evaluation"].hist()
fig = plt.figure(1, figsize=(20, 100))
fig.savefig(histUrl+'hist_last_evaluation.png', bbox_inches='tight')
plt.close(fig)

df = pd.read_excel(DataUrl,"Worksheet",parse_cols=8)
df["number_project"].hist()
fig = plt.figure(1, figsize=(20, 100))
fig.savefig(histUrl+'hist_number_project.png', bbox_inches='tight')
plt.close(fig)

df = pd.read_excel(DataUrl,"Worksheet",parse_cols=8)
df["average_montly_hours"].hist()
fig = plt.figure(1, figsize=(20, 100))
fig.savefig(histUrl+'hist_average_montly_hours.png', bbox_inches='tight')
plt.close(fig)

df = pd.read_excel(DataUrl,"Worksheet",parse_cols=8)
df["time_spend_company"].hist()
fig = plt.figure(1, figsize=(20, 100))
fig.savefig(histUrl+'hist_time_spend_company.png', bbox_inches='tight')
plt.close(fig)

df = pd.read_excel(DataUrl,"Worksheet",parse_cols=8)
df["Work_accident"].hist()
fig = plt.figure(1, figsize=(20, 100))
fig.savefig(histUrl+'hist_Work_accident.png', bbox_inches='tight')
plt.close(fig)

df = pd.read_excel(DataUrl,"Worksheet",parse_cols=8)
df["left"].hist()
fig = plt.figure(1, figsize=(20, 100))
fig.savefig(histUrl+'hist_left.png', bbox_inches='tight')
plt.close(fig)