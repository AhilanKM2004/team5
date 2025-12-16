import streamlit as st
import pandas as pd

page = st.sidebar.selectbox("Pages", ["Dashboard", "Data_Viewer", "Settings"])

if page == "Dashboard":
    st.title("Welcome to our page")
    st.header("Dashboard")
    st.image("https://i.pinimg.com/736x/37/3a/b3/373ab3e072178f47dcb7fdafaddb6854.jpg")
    st.markdown("---")
    st.write(
        "Welcome to this demo application built using Streamlit. "
        "This project is designed to showcase how simple and interactive "
        "web applications can be created using Python. "
        "It helps beginners understand basic UI components, form handling, "
        "and page layout. "
        "This demo is intended for learning and practice purposes only."
    )

elif page == "Data_Viewer":
    st.title("Data Viewer")
    file = st.file_uploader("Upload a CSV file", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        st.dataframe(df)

elif page == "Settings":
    st.title("Settings")
    region = st.text_input("Enter your region")
    volume = st.slider("Volume", 0, 100, 50)
    brightness = st.slider("Brightness", 0, 100, 50)

