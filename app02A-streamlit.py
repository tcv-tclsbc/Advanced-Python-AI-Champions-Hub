# app02.py
import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Welcome to Streamlit! Display data from a dataframe")

# Dataframe Display
st.write("Here is data from an example dataframe:")
df1 = pd.DataFrame({
    'Roll Number': [101, 102, 103, 104, 105],
    'Student Name': ['John', 'Ramesh', 'Mary', 'Bala', 'Oz']
})
st.dataframe(df1)

data = np.random.randn(50, 10) 
collist=('Col-%d' % i for i in range(10))
print(collist)
df2 = pd.DataFrame(data, columns=collist)
st.dataframe(df2)

# User Input
user_input = st.text_input("Here is data from a two dataframes:")
if user_input:
    st.write(f"Did you enjoy the response? {user_input}!")