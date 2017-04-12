## numpy is used for creating fake data
import numpy as np
import matplotlib as mpl
import pandas as pd
## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt

## Create data
df = pd.read_excel("C:/HR_Data.xlsx")

desc = df['satisfaction_level'].describe()
print(desc)

desc = df['last_evaluation'].describe()
print(desc)

desc = df['number_project'].describe()
print(desc)

desc = df['average_montly_hours'].describe()
print(desc)

desc = df['time_spend_company'].describe()
print(desc)

desc = df['Work_accident'].describe()
print(desc)

desc = df['left'].describe()
print(desc)

desc = df['promotion_last_5years'].describe()
print(desc)
