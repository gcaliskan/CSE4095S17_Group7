## numpy is used for creating fake data
import numpy as np
import matplotlib as mpl
import pandas as pd
## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt

## Create data
df = pd.read_excel("C:/test.xls")

bp = df.boxplot()


# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)


# Save the figure
fig.savefig('boxplot.png', bbox_inches='tight')