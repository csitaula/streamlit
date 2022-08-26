import streamlit as st
import pandas
import numpy

st.title("Streamlit Form Demo Revised")
#CREATING OUR FORM FIELDS
with st.form("form1", clear_on_submit=True):
    name = st.text_input("Enter full name")
    email = st.text_input("Enter email")
    message = st.text_area("Message")
    age = st.slider("Enter your age", min_value = 10, max_value = 100)
    st.write(age)
    submit=st.form_submit_button("Submit this form")
