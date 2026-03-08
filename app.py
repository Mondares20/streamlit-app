import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Helper App", layout="wide")

# ----------------- Sidebar Navigation -----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Registration", "Data", "Fun Components","About"])

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
        reg_submit= st.form_submit_button("Register")       
        if reg_submit:
            st.success(f"Registered {email} successfully!")

# ----------------- DATA PAGE -----------------
elif page == "Data":
    st.header("Student Data Table")
    # Sample data
    data = {
        "Name": ["Ashley","Christian","Jocel"],
        "Age": [20,21,22],
        "Gender": ["Female","Male","Other"],
        "Email": ["a@email.com","b@email.com","c@email.com"],
        "Year Level": [1,2,3]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)        # Component 1
    st.table(df)            # Component 2
    st.metric("Total Students", len(df))  # Component 3
    st.line_chart(df["Age"])  # Component 4
    st.bar_chart(df["Year Level"])  # Component 5

# ----------------- FUN COMPONENTS -----------------
elif page == "Fun Components":
    st.header("Fun Streamlit UI")
    st.progress(50)          # 6
    st.spinner("Loading...")  # 7
    st.balloons()             # 8
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # 9
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # 10
    st.checkbox("Check me!")   # 11
    st.radio("Pick one", ["Option A","Option B"])  # 12
    st.select_slider("Slide me", options=[1,2,3,4,5])  # 13
    st.text_area("Write something")  # 14
    st.date_input("Pick a date")  # 15
    st.time_input("Pick time")  # 16
    st.number_input("Number input")  # 17
    st.file_uploader("Upload file")  # 18
    st.color_picker("Choose color")  # 19
    st.markdown("**Styled text**")  # 20

# ----------------- ABOUT PAGE -----------------
elif page == "About":
    st.header("About This App")
    st.subheader("What the app does")
    st.write("""
    This app is a Student Helper App demonstrating a meaningful UI flow using Streamlit.
    It collects student information and showcases various Streamlit UI components.
    """)
    
    st.subheader("Target User")
    st.write("Students or beginners learning Streamlit UI components.")
    
    st.subheader("Inputs Collected")
    st.write("""
    - Name, Age, Gender, Hobbies, Birthdate  
    - Email, Password, Year Level, Favorite Color
    """)
    
    st.subheader("Outputs Shown")
    st.write("""
    - Confirmation messages  
    - Displayed user info in tables and metrics  
    - Interactive UI feedback (balloons, progress, charts)
    """)

