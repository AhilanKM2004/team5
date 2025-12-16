import streamlit as st

st.title("Registration Form")

with st.form("Registration"):
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")
    age = st.number_input("Enter your age", step=1)
    button = st.form_submit_button("Submit")

if button:
    if email and "@" in email:
        st.success("Registered Successfully")
        st.write(f"Hi {name}")
        st.write(f"Age: {age}")
        st.write(f"Email: {email}")
    else:
        st.error("Invalid Email ")


