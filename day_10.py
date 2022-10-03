import streamlit as st

st.header('st.selectbox demo')

option = st.selectbox(
    "What is your favourite colour?",
    ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Black', 'White' ), 
    index = 2,
    help = "Please select a colour from the dropdown menu."
)

st.write('Your fav. colour is: ', option)

