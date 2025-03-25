# app04.py
import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

import plotly.figure_factory as ff


# Title
st.title("Welcome to Streamlit! \n Plotting Data : Superstore Sales Analysis")

# Dataframe Display
# st.write("Here is data from an example dataframe:")
# filename = "C:\Python\00AdvancedPythonCourseJan2025\M5 L01 Streamlit\AICH_UI_Streamlit_01_SimpleApps\superstore.csv"
# filename = "./AICH_UI_Streamlit_01_SimpleApps/superstore.csv"
filename = "superstore.csv"

df = pd.read_csv(filename)

df.dropna(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Day'] = df['Order Date'].dt.day
df['DayofWeek'] = df['Order Date'].dt.dayofweek

cond1 = df['Profit'] >= 0
cond2 = df['Profit'] < 0
df.loc[cond1, 'Profit_Positive'] = df.loc[cond1, 'Profit']
df.loc[cond2, 'Profit_Negative'] = df.loc[cond2, 'Profit']


# Plot!
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]
group_labels = ['Group 1', 'Group 2', 'Group 3']
fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])

# hist_data = df['Profit_Negative']
# group_labels = df['Year']
#fig = ff.create_distplot(df['Profit_Negative'],'Sub-Category')
fig = ff.create_distplot(hist_data, group_labels)

# Plot!
st.plotly_chart(fig, use_container_width=True)
