import streamlit as st

st.header('Hello in bold')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

# st.button("I am a button.")
