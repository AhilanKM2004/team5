import streamlit as st

st.title("Calculator")

a = st.number_input("Enter first number")
b = st.number_input("Enter second number")
operation = st.selectbox("Select operation",["Add", "Subtract", "Multiply", "Divide"])
if st.button("Submit"): 
    if operation == "Add":
        add = a+b
        st.write(add)
    elif operation == "Subtract":
        sub = a-b
        st.write(sub)
    elif operation == "Multiply":
        mul = a*b
        st.write(mul)
    elif operation == "Divide":
        if num2 != 0:
            div = a/b
        st.write(div)
