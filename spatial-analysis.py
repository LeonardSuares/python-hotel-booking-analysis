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
# print(data.shape)

# Get the count of valid bookings, that are not canceled
not_cancelled = data[data['is_canceled']==0]
# print(not_cancelled)

country_wise_data = not_cancelled['country'].value_counts().reset_index()
country_wise_data.columns = ['country', 'No of guests']
# print(country_wise_data)

map_guest = px.choropleth(data_frame= country_wise_data,
                          locations=country_wise_data['country'],
                          color= country_wise_data['No of guests'],
                          hover_name= country_wise_data['country'],
                          title= "Home country of Guests"
)
map_guest.show()