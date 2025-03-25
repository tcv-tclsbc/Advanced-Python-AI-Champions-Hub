# app02.py
import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Title- Welcome to Streamlit! Two column Example")

col1, col2 = st.columns(2)
col1.write('Column 1')
col2.write('Column 2')

# Three columns with different widths
col1, col2, col3 = st.columns([1,3,1])
# col1 is wider

# Using 'with' notation:
with col1:  
     st.write('This is column 1')

with col2:  
    st.write('This is column 1')
    data = np.random.randn(50, 10) 
    collist=('Col-%d' % i for i in range(10))
    print(collist)
    df2 = pd.DataFrame(data, columns=collist)
    st.dataframe(df2)

with col3:  
     st.write('This is column 3')
