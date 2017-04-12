## numpy is used for creating fake data
import numpy as np
import matplotlib as mpl
import pandas as pd
## agg backend is used to create plot as a .png file

import matplotlib.pyplot as plt


DataUrl = "C:/HR_Data.xlsx"
## Create data
df1 = pd.read_excel(DataUrl)
df = df1[['satisfaction_level','sales']]
fig, ax = plt.subplots(figsize=(9,  6))
df.boxplot()
fig.savefig('time_spend_company.png', bbox_inches='tight')
plt.close(fig)
