import streamlit as st

st.header('st.latex demo')

st.latex(r'''
         a + ar + a r^2 + a r^3 + \cdots + r^{n-1} = 
         \sum_{k=0}^{n-1} ar^k =
         a \left(\frac{1-r^{n}}{1-r}\right) = 
         x^3 + y^{n-\left(\frac{3}{4}\right)}
         ''')

