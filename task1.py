import streamlit as st
st.header("Personal Info")

col1 ,col2, col3= st.columns(3)
name = st.write("Reeni")
image = st.image("D:/Gen AI task/image/example.png")
role = st.write("student")
edu = st.write("MCA")
skill = st.write("*Skills*-dance -sing")
contact = st.write("stanisyareeni@gmail.com")

with col2:
    st.markdown(name)
    st.markdown(image)
    st.markdown(role)
    st.markdown(edu)
    st.markdown(skill)
    st.markdown(contact)