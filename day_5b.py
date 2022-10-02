import streamlit as st
import pandas as pd

st.header("This is a header.")
st.markdown("**This** *is* some `markdown`.")
st.subheader("Subheading")
df = pd.DataFrame({
    'column_1': [1,2,3,4], 
    'column_2': [10,20,30,40]
})
st.write(df)
st.caption("This is a caption: the above is dataframe 3A")
st.text("Common, or garden, text.")
st.latex(r'''
...     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
...     \sum_{k=0}^{n-1} ar^k =
...     a \left(\frac{1-r^{n}}{1-r}\right)
...     ''')
st.code("if code = True: print('code')") 

