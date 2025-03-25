# app02.py
import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Title- Welcome to Streamlit! Example of Data Display UI Elements")

# Dataframe Display
st.write("Here is data from an example dataframe:")
st.text('This is a fixed width text')
st.markdown('This is a _Markdown_')
st.caption('This is a Caption - Just Do it by Nike..')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('For most objects') # df, err, func, keras!
st.write(['Test', 'is <', 3]) # see *
st.header('Sample Header')
st.subheader('Sample Sub-Header')
st.code('for i in range(8): foo()')

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