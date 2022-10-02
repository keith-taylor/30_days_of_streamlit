import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write demo')

st.write('Hello, *world!* : sunglasses:')

st.write(1234)

df = pd.DataFrame({
    'column_1': [1,2,3,4,5,6,7,8], 
    'column_2': [10,20,30,40,50,60,70,80]
})

st.write(df)

st.write ('Below is a dataframe:', df, "Above is a dataframe.")

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)
