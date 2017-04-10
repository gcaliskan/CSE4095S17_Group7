## numpy is used for creating fake data
import numpy as np
import matplotlib as mpl
import pandas as pd
## agg backend is used to create plot as a .png file

import matplotlib.pyplot as plt

## Create data
df = pd.read_excel("C:/orgHR_Data_v1.xls")

df1 = pd.read_excel("C:/orgHR_Data_v1.xls")
df1.plot(kind='scatter', x='satisfaction_level', y='last_evaluation');
fig1 = plt.figure(1, figsize=(9, 6))
fig1.savefig('scatterimages/scatter_satisfaction_lastevaluation.png', bbox_inches='tight')
plt.close(fig1)

df2 = pd.read_excel("C:/orgHR_Data_v1.xls")
df2.plot(kind='scatter', x='satisfaction_level', y='number_project');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_satisfaction_numberproject.png', bbox_inches='tight')
plt.close(fig2)

df2 = pd.read_excel("C:/orgHR_Data_v1.xls")
df2.plot(kind='scatter', x='satisfaction_level', y='average_montly_hours');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_satisfaction_averagemontlyhours.png', bbox_inches='tight')
plt.close(fig2)

df2 = pd.read_excel("C:/orgHR_Data_v1.xls")
df2.plot(kind='scatter', x='satisfaction_level', y='time_spend_company');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_satisfaction_timespendcompany.png', bbox_inches='tight')
plt.close(fig2)

df2 = pd.read_excel("C:/orgHR_Data_v1.xls")
df2.plot(kind='scatter', x='satisfaction_level', y='Work_accident');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_satisfaction_workaccident.png', bbox_inches='tight')
plt.close(fig2)

df2 = pd.read_excel("C:/orgHR_Data_v1.xls")
df2.plot(kind='scatter', x='satisfaction_level', y='left');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_satisfaction_left.png', bbox_inches='tight')
plt.close(fig2)

df2 = pd.read_excel("C:/orgHR_Data_v1.xls")
df2.plot(kind='scatter', x='satisfaction_level', y='promotion_last_5years');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_satisfaction_promotionlast5years.png', bbox_inches='tight')
plt.close(fig2)

df2 = pd.read_excel("C:/orgHR_Data_v1.xls")
df2.plot(kind='scatter', x='satisfaction_level', y='traffic');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_satisfaction_traffic.png', bbox_inches='tight')
plt.close(fig2)

df2 = pd.read_excel("C:/orgHR_Data_v1.xls")
df2.plot(kind='scatter', x='satisfaction_level', y='remote_work');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_satisfaction_remotework.png', bbox_inches='tight')
plt.close(fig2)

# Save the figure
