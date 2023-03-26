import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset_url = ('https://raw.githubusercontent.com/m-mehdi/pandas_tutorials/main/weekly_stocks.csv')
df = pd.read_csv(dataset_url, parse_dates=['Date'], index_col='Date')
df_3Months = df.resample(rule='M').mean()[-3:]
df_3Months.index=['March', 'April', 'May']
df_3Months.plot(kind='barh', figsize=(9,6)).get_figure().savefig('name-20')