## numpy is used for creating fake data
import numpy as np
import matplotlib as mpl
import pandas as pd
## agg backend is used to create plot as a .png file

import matplotlib.pyplot as plt

## Create data
df = pd.read_excel("C:/test.xls")

# Create a figure instance
df.plot(kind='scatter', x='number_project', y='time_spend_company');
fig = plt.figure(1, figsize=(9, 6))



# Save the figure
fig.savefig('scatter_numberproject_timespend.png', bbox_inches='tight')