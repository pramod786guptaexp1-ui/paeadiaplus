import streamlit as st
import pandas as pd
import time

# --- Google Sheets API Placeholder Function ---
# IMPORTANT: This function is a placeholder and requires you to set up the Google Sheets API.
# You will need to install the gspread and google-auth libraries and
# enable the Google Sheets API in the Google Cloud Console.
# You also need to create a service account and download its credentials.
# The `creds.json` file should be placed in your project directory.
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
 #   ------------------------------------------------------------------------
    
    # Placeholder success message for demonstration
    time.sleep(1)
    st.success("Data has been submitted successfully!")
    print(f"Data to be saved in '{sheet_name}': {data}") # Log data for local verification
    return True

# --- Page Configuration ---
st.set_page_config(
    page_title="Paeadiaplus ChildCare",
    page_icon="👶",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Sidebar Navigation ---
st.sidebar.title("Paeadiaplus ChildCare")
page = st.sidebar.radio("Navigate", ["Home", "About Us", "Our Services", "Schools", "Doctors", "News/Media", "Contact Us"])

# --- Main Page Content ---
if page == "Home":
    st.header("Welcome to Paeadiaplus ChildCare")
    st.write("Your partner in nurturing a healthier, happier future for children.")
    st.image("https://placehold.co/800x400/87CEEB/ffffff?text=Caring+for+Your+Child's+Future")
    st.markdown("""
        Paeadiaplus ChildCare is dedicated to providing comprehensive healthcare solutions for schools. 
        We believe that a healthy mind and body are the foundations of a successful education.
        Explore our services to see how we can help your school community.
    """)

elif page == "About Us":
    st.header("About Us")
    st.markdown("""
        At Paeadiaplus, we are on a mission to revolutionize school healthcare by placing a strong emphasis on mental well-being alongside physical health. 
        We believe that by integrating mental health support into the school system, we can create a nurturing environment where every child can thrive academically, emotionally, and socially. 
        
        Our team of dedicated professionals is committed to providing schools with the resources and expertise needed to address the holistic needs of their students. We partner with educational institutions to build a future where every child has the support they need to succeed.
    """)

elif page == "Our Services":
    st.header("Our Services")
    st.markdown("""
        We offer a range of specialized services designed to promote the health and well-being of the school community.
        
        * **School Doctor Check-Up Camps:** Regular health check-ups to monitor students' growth, and provide early detection of any health issues.
        * **Sex Education:** Age-appropriate and comprehensive sessions to empower students with knowledge about their bodies, relationships, and health.
        * **Seminars on Mental and Physical Health:** Engaging and informative sessions for students, teachers, and parents on topics like stress management, nutrition, and hygiene.
    """)

elif page == "Schools":
    st.header("School Registration")
    st.write("Register your school to access our specialized healthcare services.")
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
                save_to_google_sheet("School Registrations", school_data)
            else:
                st.warning("Please fill out all required fields.")
    st.write("---")
    st.write("We will contact you shortly after receiving your registration.")

elif page == "Doctors":
    st.header("Student Eye Test Data Collection")
    st.write("Enter the student's eye test details here.")
    with st.form("eye_test_form"):
        st.write("Student Details")
        student_name = st.text_input("Student Name")
        dob = st.date_input("Date of Birth")
        school_name = st.text_input("School Name")
        
        st.subheader("Eye Test Results")
        col1, col2 = st.columns(2)
        with col1:
            st.write("Right Eye (OD)")
            # Changed the label to be unique for the right eye
            od_dist_va = st.selectbox("Right Eye DVA", options=["6/6", "6/9", "6/12", "6/18", "6/24", "6/36", "6/60"])
            od_color_vision = st.selectbox("Right Eye Color Vision", options=["Normal", "Deficient"])
            
        with col2:
            st.write("Left Eye (OS)")
            # Changed the label to be unique for the left eye
            os_dist_va = st.selectbox("Left Eye DVA", options=["6/6", "6/9", "6/12", "6/18", "6/24", "6/36", "6/60"])
            os_color_vision = st.selectbox("Left Eye Color Vision", options=["Normal", "Deficient"])

        remarks = st.text_area("Remarks / Prescription (if any)")
        
        submitted = st.form_submit_button("Submit Data")
        if submitted:
            if student_name and dob and school_name:
                eye_data = [student_name, dob, school_name, od_dist_va, od_color_vision, os_dist_va, os_color_vision, remarks, pd.Timestamp.now()]
                #save_to_google_sheet("Eye Test Data", eye_data)
                # Print the data to the console
                print(eye_data)
                
                # Display the data in the Streamlit app
                st.subheader("Submitted Data")
                st.write(eye_data)
            
            else:
                st.warning("Please fill out all student details.")

elif page == "News/Media":
    st.header("News & Media")
    st.write("Stay up-to-date with our latest news and media releases.")
    st.write("Content coming soon...")

elif page == "Contact Us":
    st.header("Contact Us")
    st.write("We would love to hear from you! Please fill out the form below.")
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
