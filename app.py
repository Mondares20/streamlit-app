import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Helper App", layout="wide")

# ----------------- Sidebar Navigation -----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Registration", "Data", "Fun Components", "About"])

# ----------------- HOME PAGE -----------------
if page == "Home":
    st.title("Student Helper App")
    st.header("Welcome!")
    st.subheader("Explore Streamlit UI components")
    
    # 5 input components
    name = st.text_input("Enter your name")
    age = st.number_input("Age", 1, 100)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    hobbies = st.multiselect("Select hobbies", ["Coding", "Gaming", "Reading"])
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
        reg_submit = st.form_submit_button("Register")       
        if reg_submit:
            st.success(f"Registered {email} successfully!")

# ----------------- DATA PAGE -----------------
elif page == "Data":
    st.header("Student Data Table")
    
    # Realistic student data
    data = {
        "Name": ["Ashley Abrantes", "Christian Basilan", "Jocel Pasko", "Ej Ellegue", "Diana Gaviola"],
        "Email": [
            "2024-200314@rtu.edu.ph",
            "2024-200201@rtu.edu.ph",
            "2024-200305@rtu.edu.ph",
            "2024-200110@rtu.edu.ph",
            "2022-200402@rtu.edu.ph"
        ],
        "Year Level": [2, 2, 2, 2, 2],
        "Gender": ["Female", "Male", "Female", "Male", "Female"],
        "Hobbies": [
            "Coding, Reading",
            "Gaming, Reading",
            "Coding, Gaming",
            "Sports, Gaming",
            "Reading, Art"
        ],
        "Favorite Color": ["#FF5733", "#33FF57", "#3357FF", "#33FF57", "#FF33A1"],
        "Birthdate": ["2002-10-13", "2002-06-18", "2005-10-30", "2003-03-15", "2004-08-22"]
    }

    df = pd.DataFrame(data)
    st.table(df)
    st.subheader("Summary Metrics")
    st.metric("Total Students", len(df))
    st.bar_chart(df["Year Level"])

# ----------------- FUN COMPONENTS -----------------
elif page == "Fun Components":
    st.header("Fun Components Demo")
    
    st.subheader("Progress bar")
    progress = st.progress(0)
    for i in range(101):
        progress.progress(i)

    st.subheader("Interactive Widgets")
    color = st.color_picker("Pick your favorite color")
    st.write("You selected:", color)

    sound_option = st.selectbox("Choose sound effect", ["None", "Beep", "Chime"])
    st.write("Selected sound:", sound_option)

    st.subheader("Playful UI")
    st.balloons()
    with st.spinner("Simulating loading..."):
        st.text("Loading complete!")

    # Extra fun components
    age_slider = st.slider("Choose your age", 1, 100)
    agree_checkbox = st.checkbox("Do you agree to fun terms?")
    st.text_area("Write something fun here:")
    st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])
    st.select_slider("Select a range", options=list(range(0, 11)))
    st.button("Click me!")
    st.caption("This section demonstrates playful and interactive Streamlit components!")

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
    - Interactive UI feedback (balloons, progress bar, charts)
    """)
