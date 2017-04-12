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

df = df[df.salary != 'low']
df = df[df.salary != 'medium']

#ax = df.average_montly_hours.plot(xticks=df.index, rot=90)
#ax.set_xticklabels(df.sales)

groups = df.groupby('salary')

fig, ax = plt.subplots()
ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
for name, group in groups:
    ax.plot(group.average_montly_hours, group.number_project, marker='o', linestyle='', ms=12, label=name)
ax.legend()

fig2 = plt.figure(1, figsize=(9, 6))

fig2.savefig('compare/montlyhours_left_high.png', bbox_inches='tight')
