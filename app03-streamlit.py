# app02.py
import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

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
cond1 = df['Year'] == 2018
cond2 = df['Year'] == 11

df_nov = df[cond1 & cond2]

df['Month'] = df['Order Date'].dt.month
df['Day'] = df['Order Date'].dt.day
df['DayofWeek'] = df['Order Date'].dt.dayofweek

segment = df['Segment'].value_counts()

#create figure instance (Canvas)
st.bar_chart(df, x="Year", y="Sales", color="Segment")

# st.line_chart(df, x="Year", y="Quantity")


