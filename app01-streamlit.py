# app01.py
import streamlit as st

# Title
st.title("Welcome to Streamlit!")

# Dataframe Display
st.write("Hello ! What is your name?")

user_input = st.text_input("Enter your name:")
if user_input:
    st.write(f"Hello, {user_input}!")

import streamlit as st
import pandas as pd

# Title
st.title("Welcome to Streamlit! App 02")

# Dataframe Display
st.write("Here's an example dataframe:")
df = pd.DataFrame({
    'Column A': [1, 2, 3],
    'Column B': [4, 5, 6]
})
st.dataframe(df)

# User Input
user_input = st.text_input("Enter your name:")
if user_input:
    st.write(f"Hello, {user_input}!")