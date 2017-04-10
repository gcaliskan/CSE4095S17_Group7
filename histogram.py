## numpy is used for creating fake data
import numpy as np
import matplotlib as mpl
import pandas as pd
## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt

## Create data
df = pd.read_excel("C:/HR_Data.xlsx")


df.plot.hist(alpha=0.5)
# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))



# Save the figure
fig.savefig('histogram.png', bbox_inches='tight')