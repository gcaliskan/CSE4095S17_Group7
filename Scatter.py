## numpy is used for creating fake data
import numpy as np
import matplotlib as mpl
import pandas as pd
## agg backend is used to create plot as a .png file

import matplotlib.pyplot as plt


DataUrl = "C:/HR_Data.xlsx"
## Create data
df = pd.read_excel(DataUrl)

df1 = pd.read_excel(DataUrl)
df1.plot(kind='scatter', x='satisfaction_level', y='last_evaluation');
fig1 = plt.figure(1, figsize=(9, 6))
fig1.savefig('scatterimages/scatter_satisfaction_lastevaluation.png', bbox_inches='tight')
plt.close(fig1)

df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='satisfaction_level', y='number_project');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_satisfaction_numberproject.png', bbox_inches='tight')
plt.close(fig2)

df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='satisfaction_level', y='average_montly_hours');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_satisfaction_averagemontlyhours.png', bbox_inches='tight')
plt.close(fig2)

df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='satisfaction_level', y='time_spend_company');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_satisfaction_timespendcompany.png', bbox_inches='tight')
plt.close(fig2)

df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='satisfaction_level', y='Work_accident');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_satisfaction_workaccident.png', bbox_inches='tight')
plt.close(fig2)

df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='satisfaction_level', y='left');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_satisfaction_left.png', bbox_inches='tight')
plt.close(fig2)

df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='satisfaction_level', y='promotion_last_5years');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_satisfaction_promotionlast5years.png', bbox_inches='tight')
plt.close(fig2)




df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='last_evaluation', y='number_project');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_last_evaluation_numberproject.png', bbox_inches='tight')
plt.close(fig2)

df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='last_evaluation', y='average_montly_hours');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_last_evaluation_averagemonthlyhours.png', bbox_inches='tight')
plt.close(fig2)

df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='last_evaluation', y='time_spend_company');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_last_evaluation_timespendcompany.png', bbox_inches='tight')
plt.close(fig2)

df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='last_evaluation', y='Work_accident');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_last_evaluation_workaccident.png', bbox_inches='tight')
plt.close(fig2)

df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='last_evaluation', y='left');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_last_evaluation_left.png', bbox_inches='tight')
plt.close(fig2)

df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='last_evaluation', y='promotion_last_5years');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_last_evaluation_promotionlast5years.png', bbox_inches='tight')
plt.close(fig2)





df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='average_montly_hours', y='time_spend_company');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_averagemontlyhours_timespend.png', bbox_inches='tight')
plt.close(fig2)


df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='average_montly_hours', y='Work_accident');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_averagemontlyhours_workaccident.png', bbox_inches='tight')
plt.close(fig2)


df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='average_montly_hours', y='left');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_averagemontlyhours_left.png', bbox_inches='tight')
plt.close(fig2)

df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='average_montly_hours', y='promotion_last_5years');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_averagemontlyhours_promotionlast5years.png', bbox_inches='tight')
plt.close(fig2)



df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='time_spend_company', y='Work_accident');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_timespend_promotionlast5years.png', bbox_inches='tight')
plt.close(fig2)


df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='time_spend_company', y='left');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_timespend_left.png', bbox_inches='tight')
plt.close(fig2)


df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='time_spend_company', y='promotion_last_5years');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_timespend_promotionlast5years.png', bbox_inches='tight')
plt.close(fig2)




df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='Work_accident', y='left');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_workaccident_left.png', bbox_inches='tight')
plt.close(fig2)


df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='Work_accident', y='promotion_last_5years');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_workaccident_promotionlast5years.png', bbox_inches='tight')
plt.close(fig2)


df2 = pd.read_excel(DataUrl)
df2.plot(kind='scatter', x='left', y='promotion_last_5years');
fig2 = plt.figure(1, figsize=(9, 6))
fig2.savefig('scatterimages/scatter_left_promotionlast5years.png', bbox_inches='tight')
plt.close(fig2)


















