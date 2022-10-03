import streamlit as st

st.header('st.multiselect demo')

options = st.multiselect(
    'What are you favourite colours?',
    ['Red', 'Orange', 'Green', 'Blue', 'Black', 'White'],
    help="Select yourfavourite colours."
)

st.write("you chose the following: ", options)