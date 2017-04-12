## numpy is used for creating fake data
import numpy as np
import matplotlib as mpl
import pandas as pd
## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt

DataUrl = "C:/HR_Data.xlsx"
boxplotUrl="categoricalboxplots/"

## Create data
df = pd.read_excel(DataUrl)

df = df[df.salary != 'high']
df = df[df.salary != 'low']

fig, ax = plt.subplots(figsize=(9,  6))
df.boxplot([3])
fig.savefig(boxplotUrl+'motlyhour_medium.png', bbox_inches='tight')
plt.close(fig)
