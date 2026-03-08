import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Helper App", layout="wide")

# ----------------- Sidebar Navigation -----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Registration", "Data", "About", "Fun Components"])

# ----------------- HOME PAGE -----------------
if page == "Home":
    st.title("Student Helper App")
    st.header("Welcome!")
    st.subheader("Explore Streamlit UI components")
    
    # 5 inputs
    name = st.text_input("Enter your name")
    age = st.number_input("Age", 1, 100)
    gender = st.selectbox("Gender", ["Male","Female","Other"])
    hobbies = st.multiselect("Select hobbies", ["Coding","Gaming","Reading"])
    birthdate = st.date_input("Birthdate")
    
    agree = st.checkbox("I agree to terms")
    
    if st.button("Submit"):
        st.success(f"Hello {name}! Your info has been submitted.")

# ----------------- REGISTRATION PAGE -----------------
elif page == "Registration":
    st.header("Student Registration Form")
    with st.form("reg_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        level = st.slider("Year Level", 1, 4)
        color = st.color_picker("Pick your favorite color")
        submit = st.form_submit_button("Submit")
        if submit:
            st.success("Registration submitted!")

# ----------------- DATA PAGE -----------------
elif page == "Data":
    st.title("Data Page")
    st.write("Sample Data Table")

# ----------------- FUN COMPONENTS -----------------
elif page == "Fun Components":
    st.title("Fun Components")
    st.balloons()

# ----------------- ABOUT PAGE -----------------
elif page == "About":
    st.title("About")
    st.write("This app is created using Streamlit.")
