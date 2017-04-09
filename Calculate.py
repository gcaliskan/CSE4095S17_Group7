import xlrd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("C:/test.xls")
print(df.mean())
print(df.std())
print(df.var())
print(df.median())
print(df.mode())

