from operator import index
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header('Demonstration of a line chart!')



raw_data = pd.DataFrame(
    np.random.randn(20,2), 
    columns=['prop', 'spec']
    )


st.line_chart(data=raw_data, x="prop", y='spec')


