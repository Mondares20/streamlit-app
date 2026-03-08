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
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    hobbies = st.multiselect("Select hobbies", ["Coding","Gaming","Reading","Music","Sports"])
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
        file = st.file_uploader("Upload profile picture")
        submitted = st.form_submit_button("Register")
        if submitted:
            st.success("Registered Successfully!")
            st.balloons()

# ----------------- DATA PAGE -----------------
elif page == "Data":
    st.header("Sample Data Visualization")
    data = {
        "Name":["Ana","Ben","Carl","Dina","Evan"],
        "Score":[90,85,88,92,80]
    }
    df = pd.DataFrame(data)

    st.dataframe(df)
    st.table(df)
    st.bar_chart(df["Score"])
    st.line_chart(df["Score"])
    st.area_chart(df["Score"])

# ----------------- FUN COMPONENTS PAGE -----------------
elif page == "Fun Components":
    st.header("Fun Components for Extra Merit Points")
    st.progress(0.7)
    st.metric("Attendance", "85%", "5% from last week")
    st.info("Did you know? Streamlit is amazing!")
    st.warning("This is just a demo warning!")
    st.error("Error example")
    st.success("Success example")
    st.toast("This is a toast notification!")  # works in latest Streamlit
    st.divider()
    tab1, tab2, tab3 = st.tabs(["Tab 1","Tab 2","Tab 3"])
    with tab1:
        st.write("Welcome to Tab 1")
    with tab2:
        st.write("Welcome to Tab 2")
    with tab3:
        st.write("Welcome to Tab 3")

# ----------------- ABOUT PAGE -----------------
elif page == "About":
    st.header("About This App")
    st.write("""
    **What the app does:**  
    Collects student info, shows data, and demonstrates Streamlit UI components.

    **Target users:**  
    Students and beginners learning Streamlit.

    **Inputs:**  
    Name, age, gender, hobbies, birthdate, email, password, year level, favorite color, file uploads.

    **Outputs:**  
    Confirmation messages, tables, charts, and interactive components.
    """)
