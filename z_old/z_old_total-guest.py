import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

import  chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px

from plotly.offline import download_plotlyjs, init_notebook_mode, plot

# 1. Shows all columns (You already have this)
pd.set_option('display.max_columns', None)

# 2. DISABLES WRAPPING by setting the display width to a very high number
pd.set_option('display.width', 1000)

import  warnings
from warnings import filterwarnings
filterwarnings("ignore")

df = pd.read_csv(r"C:\Users\leona\PycharmProjects\Python Data Analysis Projects\Hotel-bookings-analysis\hotel_bookings.csv")
# print(df.head(5))

filter1 = (df['children']==0) & (df['adults']==0) & (df['babies']==0)

df2 = df[~filter1]
# print(df2.shape)
# print(df2.duplicated().sum())
data = df2.drop_duplicates()



dict_month = {'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12, 'January':1,
 'February':2, 'March':3, 'April':4, 'May':5, 'June':6}
data['arrival_date_month_index'] = data['arrival_date_month'].map(dict_month)

# print(data[['arrival_date_year', 'arrival_date_month_index','arrival_date_day_of_month']])
data['arrival_date'] = data['arrival_date_year'].astype(str)+'-'+data['arrival_date_month_index'].astype(str)+'-'+data['arrival_date_day_of_month'].astype(str)
data['Total_guests'] = data['adults']+data['children']+data['babies']
data_not_canceled = data[data['is_canceled']==0]
guest_arrival_series = data_not_canceled.groupby(['arrival_date'])['Total_guests'].sum()
# guest_arrival_series.plot(figsize=(10,6))
sns.displot(guest_arrival_series.values, kind='kde')
plt.show()
