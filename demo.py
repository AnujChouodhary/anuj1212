
import streamlit as st

st.title("Addition App")

a = st.number_input("Enter first number", value=0)
b = st.number_input("Enter second number", value=0)

if st.button("Add"):
    result = a + b
    st.success(f"Result: {result}")

