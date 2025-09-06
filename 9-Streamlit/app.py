"""#### Introduction to Streamlit
    Streamlit is an open-source app framework for Machine Learning 
    and Data Science projects. It allows you to create beautiful 
    web applications for your machine learning and data science projects 
    with simple Python scripts.
"""

import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hello Streamlit")

## Diplay a Simple Text
st.write("This is a simple text")

##create a simple Dataframe

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})


## Display the Dataframe
st.write("Here is the dataframe")
st.write(df)


##create a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)