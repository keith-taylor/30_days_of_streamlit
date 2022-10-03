import streamlit as st

st.header("st.checkbox demo!")

st.write("What would you like to order?")

ice_cream = st.checkbox('Ice Cream', help = "Please select for eatings.")
coffee = st.checkbox('Coffee', help = "Please select for to drink.")
cola = st.checkbox('Cola-Cola', help = "Please select for to drink.")
vanilla_toast = st.checkbox('Toast (vanilla style)', help = "Please select for eatings.")
karky_kind = st.checkbox('Pudding (Karky style', help = "Please select for eatings.")
i_can_i_cant = st.checkbox('I can of can\'t', help = "Please select for to drink.")
melberry_fresh = st.checkbox('Fresh Mellberry (iced jar)', help = "Please select for eatings.")


if ice_cream:
    st.write("Okay, here's some ice cream 🍦")
if coffee:
    st.write("Okay, here's some coffee ☕️")
if cola:
    st.write("Okay, here's some cola 🥤")
if vanilla_toast:
    st.write("Okay, here's some vanilla toast 🍞")
if karky_kind:
    st.write("Okay, here's some karky kind 🍡")
if i_can_i_cant:
    st.write("Okay, here's a can I can't 🥫")
if melberry_fresh:
    st.write("Okay, here's some fresh melberry 🫐")
