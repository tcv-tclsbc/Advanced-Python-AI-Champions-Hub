# app02.py
import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Title- Welcome to Streamlit! Example of Input Values")

st.button('Button : Hit me')
st.checkbox('Checkbox 1')
st.radio('Pick one:', ['Red','Blue', 'Green'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('This is a Slider', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text - your name')
st.number_input('Enter a number')
st.text_area('Broader Text Area Textual entry')
st.date_input('Input a Date Value')
st.time_input('Input a Time Value')
st.file_uploader('File uploader')
st.color_picker('Pick a color')

data = np.random.randn(50, 10) 
collist=('Col-%d' % i for i in range(10))
print(collist)
df2 = pd.DataFrame(data, columns=collist)
st.dataframe(df2)
st.data_editor('Please Edit data', data)
