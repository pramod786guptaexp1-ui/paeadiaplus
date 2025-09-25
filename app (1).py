import streamlit as st
import pandas as pd
import time
import textwrap
import pdfkit

def generate_llm_summary(data):
    """
    Simulates an API call to an open-source LLM to generate a summary.
    Replace this with your actual LLM integration code.
    """
    prompt = f"""
    Based on the following student's eye test data, generate a concise and clear medical summary in a professional tone. 
    Highlight any potential issues or recommendations.
    
    Data:
    Student Name: {data['Student Name']}
    Date of Birth: {data['Date of Birth']}
    School Name: {data['School Name']}
    Right Eye DVA: {data['Right Eye DVA']}
    Right Eye Color Vision: {data['Right Eye Color Vision']}
    Left Eye DVA: {data['Left Eye DVA']}
    Left Eye Color Vision: {data['Left Eye Color Vision']}
    Remarks: {data['Remarks']}
    """
    
    # --- This part is a placeholder ---
    # In a real app, you would send 'prompt' to your LLM API and get a response.
    # For example, using the Hugging Face API or a local model.
    # response = llm_api_call(prompt)
    
    # Placeholder response for demonstration
    summary = f"""
    ### Eye Test Summary for {data['Student Name']}
    
    **Patient Information:**
    - **Name:** {data['Student Name']}
    - **Date of Birth:** {data['Date of Birth']}
    - **School:** {data['School Name']}
    
    **Vision Acuity:**
    - **Right Eye:** The patient's distance vision acuity (DVA) for the right eye is {data['Right Eye DVA']}.
    - **Left Eye:** The patient's distance vision acuity (DVA) for the left eye is {data['Left Eye DVA']}.
    
    **Color Vision:**
    - **Right Eye:** Color vision for the right eye is reported as **{data['Right Eye Color Vision']}**.
    - **Left Eye:** Color vision for the left eye is reported as **{data['Left Eye Color Vision']}**.
    
    **Findings & Recommendations:**
    {data['Remarks'] if data['Remarks'] else 'No specific remarks were noted during the examination.'}
    """
    return textwrap.dedent(summary)

def generate_pdf_report(llm_summary, data):
    """
    Generates a PDF report from the LLM summary and raw data.
    """
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Eye Report for {data['Student Name']}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1, h2 {{ color: #004d40; }}
            .data-section {{ margin-bottom: 20px; padding: 10px; border: 1px solid #e0e0e0; border-radius: 5px; }}
            .llm-summary {{ background-color: #f1f8e9; padding: 15px; border-radius: 5px; }}
            .field-label {{ font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>Paeadiaplus ChildCare - Eye Report</h1>
        <h2>Student Information</h2>
        <div class="data-section">
            <p><span class="field-label">Student Name:</span> {data['Student Name']}</p>
            <p><span class="field-label">Date of Birth:</span> {data['Date of Birth']}</p>
            <p><span class="field-label">School Name:</span> {data['School Name']}</p>
        </div>
        <h2>Eye Test Results</h2>
        <div class="data-section">
            <p><span class="field-label">Right Eye DVA:</span> {data['Right Eye DVA']}</p>
            <p><span class="field-label">Right Eye Color Vision:</span> {data['Right Eye Color Vision']}</p>
            <p><span class="field-label">Left Eye DVA:</span> {data['Left Eye DVA']}</p>
            <p><span class="field-label">Left Eye Color Vision:</span> {data['Left Eye Color Vision']}</p>
            <p><span class="field-label">Remarks:</span> {data['Remarks']}</p>
        </div>
        <h2>LLM Report Summary</h2>
        <div class="llm-summary">
            {llm_summary.replace('\n', '<br>')}
        </div>
    </body>
    </html>
    """
    
    # Configure pdfkit to point to the wkhtmltopdf executable
    path_to_wkhtmltopdf = '/usr/bin/wkhtmltopdf'  # This is the common path on Linux systems
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
    
    # Pass the configuration to the from_string method
    pdf = pdfkit.from_string(html_content, False, configuration=config)
    
    return pdf
    
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
    st.image("https://images.pexels.com/photos/4033148/pexels-photo-4033148.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="Caring for Your Child's Future", use_container_width=True)
    st.markdown("""
        Paediaplus ChildCare is dedicated to providing comprehensive healthcare solutions for schools. 
        We believe that a healthy mind and body are the foundations of a successful education.
        Explore our services to see how we can help your school community.
    """)
    st.image("https://images.pexels.com/photos/4021775/pexels-photo-4021775.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="A warm and friendly environment", use_container_width=True)

elif page == "About Us":
    st.header("About Us")
    st.image("https://images.pexels.com/photos/5407008/pexels-photo-5407008.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="Our team is dedicated to your child's well-being", use_container_width=True)
    st.markdown("""
        At Paediaplus, we are on a mission to revolutionize school healthcare by placing a strong emphasis on mental well-being alongside physical health. 
        We believe that by integrating mental health support into the school system, we can create a nurturing environment where every child can thrive academically, emotionally, and socially. 
        
        Our team of dedicated professionals is committed to providing schools with the resources and expertise needed to address the holistic needs of their students. We partner with educational institutions to build a future where every child has the support they need to succeed.
    """)
    st.image("https://images.pexels.com/photos/4167542/pexels-photo-4167542.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="Child-friendly health check-ups", use_container_width=True)

elif page == "Our Services":
    st.header("Our Services")
    # Changed image to a doctor treating a child
    st.image("https://images.pexels.com/photos/4021779/pexels-photo-4021779.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="Dedicated doctors caring for your child", use_container_width=True)
    st.markdown("""
        We offer a range of specialized services designed to promote the health and well-being of the school community.
        
        * **School Doctor Check-Up Camps:** Regular health check-ups to monitor students' growth, and provide early detection of any health issues.
        * **Sex Education:** Age-appropriate and comprehensive sessions to empower students with knowledge about their bodies, relationships, and health.
        * **Seminars on Mental and Physical Health:** Engaging and informative sessions for students, teachers, and parents on topics like stress management, nutrition, and hygiene.
    """)
    st.image("https://images.pexels.com/photos/3845946/pexels-photo-3845946.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="Learning and growing together", use_container_width=True)

elif page == "Schools":
    st.header("School Registration")
    st.write("Register your school to access our specialized healthcare services.")
    # Changed image to a school building
    st.image("https://images.pexels.com/photos/207691/pexels-photo-207691.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="Partner with us for a healthier school environment", use_container_width=True)
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
    st.image("https://images.pexels.com/photos/3771120/pexels-photo-3771120.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="Eye examinations are quick and easy", use_container_width=True)
    
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
                eye_data = {
                    "Student Name": student_name,
                    "Date of Birth": dob.strftime("%Y-%m-%d"),
                    "School Name": school_name,
                    "Right Eye DVA": od_dist_va,
                    "Right Eye Color Vision": od_color_vision,
                    "Left Eye DVA": os_dist_va,
                    "Left Eye Color Vision": os_color_vision,
                    "Remarks": remarks
                }
                
                # --- LLM API Call and Summary Generation ---
                st.subheader("Report Summary")
                st.info("Generating summary using Open Source LLM...")
                
                # Placeholder for LLM API call
                llm_response = generate_llm_summary(eye_data)
                
                st.markdown(llm_response)
                
                # --- PDF Generation and Download ---
                st.subheader("Download Report")
                pdf_file = generate_pdf_report(llm_response, eye_data)
                
                st.download_button(
                    label="Download Report as PDF",
                    data=pdf_file,
                    file_name=f"{student_name}_Eye_Report.pdf",
                    mime="application/pdf"
                )
                
            else:
                st.warning("Please fill out all student details.")

elif page == "News/Media":
    st.header("News & Media")
    st.image("https://images.pexels.com/photos/4033146/pexels-photo-4033146.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="In the news and media", use_container_width=True)
    st.write("Stay up-to-date with our latest news and media releases.")
    st.write("Content coming soon...")

elif page == "Contact Us":
    st.header("Contact Us")
    st.write("We would love to hear from you! Please fill out the form below.")
    st.image("https://images.pexels.com/photos/4033150/pexels-photo-4033150.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", caption="Get in touch with us", use_container_width=True)
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
