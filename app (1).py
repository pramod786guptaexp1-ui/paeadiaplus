import streamlit as st
import pandas as pd
import time

# --- Google Sheets API Placeholder Function ---
def save_to_google_sheet(sheet_name, data):
    """
    Saves form data to a Google Sheet. This is a placeholder function.
    You need to implement the actual API calls.
    """
    st.info("Simulating data submission to Google Sheets...")
    # --- Uncomment and configure this section to use the Google Sheets API ---
    try:
        import gspread
        from google.oauth2.service_account import Credentials
        
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = Credentials.from_service_account_file('creds.json', scopes=scope)
        client = gspread.authorize(creds)
        
        # Open the Google Sheet by its name or URL
        spreadsheet = client.open(sheet_name)
        worksheet = spreadsheet.sheet1
        
        # Append the data row
        worksheet.append_row(data)
        st.success("Data successfully saved to Google Sheet!")
        return True
    except Exception as e:
        st.error(f"Failed to save data to Google Sheets: {e}")
        return False
    
    # Placeholder success message for demonstration
    time.sleep(1)
    st.success("Data has been submitted successfully!")
    print(f"Data to be saved in '{sheet_name}': {data}") # Log data for local verification
    return True

# --- Page Configuration ---
st.set_page_config(
    page_title="Paediaplus ChildCare",
    page_icon="👶",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Sidebar Navigation ---
st.sidebar.title("Paediaplus ChildCare")
page = st.sidebar.radio("Navigate", ["Home", "About Us", "Our Services", "Schools", "Doctors", "News/Media", "Contact Us"])

# --- Main Page Content ---
if page == "Home":
    st.header("Welcome to Paediaplus ChildCare")
    st.write("Your partner in nurturing a healthier, happier future for children.")
    # Image with specified width
    st.image("https://images.pexels.com/photos/4033148/pexels-photo-4033148.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="Caring for Your Child's Future", width=600, height=300)
    st.markdown("""
        Paediaplus ChildCare is dedicated to providing comprehensive healthcare solutions for schools. 
        We believe that a healthy mind and body are the foundations of a successful education.
        Explore our services to see how we can help your school community.
    """)
    st.image("https://images.pexels.com/photos/4021775/pexels-photo-4021775.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="A warm and friendly environment", width=600, height=300)

elif page == "About Us":
    st.header("About Us")
    st.image("https://images.pexels.com/photos/5407008/pexels-photo-5407008.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="Our team is dedicated to your child's well-being", width=600, height=300)
    st.markdown("""
        At Paediaplus, we are on a mission to revolutionize school healthcare by placing a strong emphasis on mental well-being alongside physical health. 
        We believe that by integrating mental health support into the school system, we can create a nurturing environment where every child can thrive academically, emotionally, and socially. 
        
        Our team of dedicated professionals is committed to providing schools with the resources and expertise needed to address the holistic needs of their students. We partner with educational institutions to build a future where every child has the support they need to succeed.
    """)
    st.image("https://images.pexels.com/photos/4167542/pexels-photo-4167542.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="Child-friendly health check-ups", width=600, height=300)

elif page == "Our Services":
    st.header("Our Services")
    st.image("https://images.pexels.com/photos/4167540/pexels-photo-4167540.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="Comprehensive health services for schools", width=600, height=300)
    st.markdown("""
        We offer a range of specialized services designed to promote the health and well-being of the school community.
        
        * **School Doctor Check-Up Camps:** Regular health check-ups to monitor students' growth, and provide early detection of any health issues.
        * **Sex Education:** Age-appropriate and comprehensive sessions to empower students with knowledge about their bodies, relationships, and health.
        * **Seminars on Mental and Physical Health:** Engaging and informative sessions for students, teachers, and parents on topics like stress management, nutrition, and hygiene.
    """)
    st.image("https://images.pexels.com/photos/3845946/pexels-photo-3845946.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="Learning and growing together", width=600, height=300)

elif page == "Schools":
    st.header("School Registration")
    st.write("Register your school to access our specialized healthcare services.")
    st.image("https://images.pexels.com/photos/4167543/pexels-photo-4167543.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="Partner with us to create a healthier school environment", width=600, height=300)
    with st.form("school_registration_form"):
        st.write("School Information")
        school_name = st.text_input("School Name")
        contact_person = st.text_input("Contact Person")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        message = st.text_area("Why are you interested in our services?")
        
        submitted = st.form_submit_button("Register School")
        if submitted:
            if school_name and contact_person and email and phone:
                school_data = [school_name, contact_person, email, phone, message, pd.Timestamp.now()]
                print(school_data)
                st.subheader("Submitted School Data")
                st.write(school_data)
            else:
                st.warning("Please fill out all required fields.")
    st.write("---")
    st.write("We will contact you shortly after receiving your registration.")
    
elif page == "Doctors":
    st.header("Student Eye Test Data Collection")
    st.write("Enter the student's eye test details here.")
    st.image("https://images.pexels.com/photos/3771120/pexels-photo-3771120.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="Eye examinations are quick and easy", width=600, height=300)
    with st.form("eye_test_form"):
        st.write("Student Details")
        student_name = st.text_input("Student Name")
        dob = st.date_input("Date of Birth")
        school_name = st.text_input("School Name")
        
        st.subheader("Eye Test Results")
        col1, col2 = st.columns(2)
        with col1:
            st.write("Right Eye (OD)")
            od_dist_va = st.selectbox("Right Eye DVA", options=["6/6", "6/9", "6/12", "6/18", "6/24", "6/36", "6/60"])
            od_color_vision = st.selectbox("Right Eye Color Vision", options=["Normal", "Deficient"])
            
        with col2:
            st.write("Left Eye (OS)")
            os_dist_va = st.selectbox("Left Eye DVA", options=["6/6", "6/9", "6/12", "6/18", "6/24", "6/36", "6/60"])
            os_color_vision = st.selectbox("Left Eye Color Vision", options=["Normal", "Deficient"])

        remarks = st.text_area("Remarks / Prescription (if any)")
        
        submitted = st.form_submit_button("Submit Data")
        if submitted:
            if student_name and dob and school_name:
                eye_data = [student_name, dob, school_name, od_dist_va, od_color_vision, os_dist_va, os_color_vision, remarks, pd.Timestamp.now()]
                print(eye_data)
                st.subheader("Submitted Data")
                st.write(eye_data)
            else:
                st.warning("Please fill out all student details.")

elif page == "News/Media":
    st.header("News & Media")
    st.image("https://images.pexels.com/photos/4033146/pexels-photo-4033146.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="In the news and media", width=600, height=300)
    st.write("Stay up-to-date with our latest news and media releases.")
    st.write("Content coming soon...")

elif page == "Contact Us":
    st.header("Contact Us")
    st.write("We would love to hear from you! Please fill out the form below.")
    st.image("https://images.pexels.com/photos/4033150/pexels-photo-4033150.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="Get in touch with us", width=600, height=300)
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        
        submitted = st.form_submit_button("Send Message")
        if submitted:
            if name and email and message:
                contact_data = [name, email, message, pd.Timestamp.now()]
                save_to_google_sheet("Contact Us Messages", contact_data)
            else:
                st.warning("Please fill out all fields.")
