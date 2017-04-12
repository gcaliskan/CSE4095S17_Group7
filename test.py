## numpy is used for creating fake data
import numpy as np
import matplotlib as mpl
import pandas as pd
## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt

DataUrl = "C:/HR_Data.xlsx"
boxplotUrl="boxplots/"

## Create data
df = pd.read_excel(DataUrl)
fig, ax = plt.subplots(figsize=(9,  6))
df.boxplot([0])
fig.savefig(boxplotUrl+'satisfaction_level.png', bbox_inches='tight')
plt.close(fig)

df = pd.read_excel(DataUrl)
fig, ax = plt.subplots(figsize=(9,  6))
df.boxplot([1])
fig.savefig(boxplotUrl+'last_evaluation.png', bbox_inches='tight')
plt.close(fig)


df = pd.read_excel(DataUrl)
fig, ax = plt.subplots(figsize=(9,  6))
df.boxplot([2])
fig.savefig(boxplotUrl+'number_project.png', bbox_inches='tight')
plt.close(fig)


df = pd.read_excel(DataUrl)
fig, ax = plt.subplots(figsize=(9,  6))
df.boxplot([3])
fig.savefig(boxplotUrl+'average_montly_hours.png', bbox_inches='tight')
plt.close(fig)


df = pd.read_excel(DataUrl)
fig, ax = plt.subplots(figsize=(9,  6))
df.boxplot([4])
fig.savefig(boxplotUrl+'time_spend_company.png', bbox_inches='tight')
plt.close(fig)


df = pd.read_excel(DataUrl)
fig, ax = plt.subplots(figsize=(9,  6))
df.boxplot([5])
fig.savefig(boxplotUrl+'Work_accident.png', bbox_inches='tight')
plt.close(fig)

df = pd.read_excel(DataUrl)
fig, ax = plt.subplots(figsize=(9,  6))
df.boxplot([6])
fig.savefig(boxplotUrl+'left.png', bbox_inches='tight')
plt.close(fig)

df = pd.read_excel(DataUrl)
fig, ax = plt.subplots(figsize=(9,  6))
df.boxplot([7])
fig.savefig(boxplotUrl+'promotion_last_5years.png', bbox_inches='tight')
plt.close(fig)

