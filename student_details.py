import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import streamlit as st
import zipfile
import io

# Function to create a PDF from student data
def create_pdf(row, output_dir):
    pdf_file_path = os.path.join(output_dir, f"{row.get('Name', 'student')}_output.pdf")
    c = canvas.Canvas(pdf_file_path, pagesize=letter)
    width, height = letter
    y = height - 50

    # Add content to the PDF
    c.drawString(100, y, f"Name: {row.get('Name', 'N/A')}")
    y -= 20
    c.drawString(100, y, f"University: {row.get('University', 'N/A')}")
    y -= 20
    c.drawString(100, y, f"Roll Number: {row.get('Roll Number', 'N/A')}")
    y -= 20
    c.drawString(100, y, f"Institute: {row.get('Institute', 'N/A')}")
    y -= 20
    c.drawString(100, y, f"Class: {row.get('Class', 'N/A')}")
    y -= 20
    c.drawString(100, y, f"Company State: {row.get('Company State', 'N/A')}")
    y -= 20
    c.drawString(100, y, f"Company Country: {row.get('Company Country', 'N/A')}")
    y -= 20
    c.drawString(100, y, f"Date of Issuance: {row.get('Date of Issuance', 'N/A')}")
    y -= 20
    c.drawString(100, y, f"Serial Number: {row.get('Serial Number', 'N/A')}")
    y -= 20
    c.drawString(100, y, f"QR URL: {row.get('QR URL', 'N/A')}")

    c.save()
    return pdf_file_path  # Return the path to the generated PDF

# Function to create a zip file of all PDFs
def create_zip(output_dir):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as z:
        for file_name in os.listdir(output_dir):
            if file_name.endswith('.pdf'):
                z.write(os.path.join(output_dir, file_name), file_name)
    zip_buffer.seek(0)
    return zip_buffer

# Streamlit UI
st.title("Certificates")
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    # Read the uploaded Excel file
    student_data = pd.read_excel(uploaded_file)
    
    output_dir = 'student_pdfs'
    os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

    # Generate PDFs for each student
    for index, row in student_data.iterrows():
        create_pdf(row, output_dir)  # Create PDF for the student

    st.success("Certificates generated successfully!")

    # Create a zip file of all generated PDFs
    zip_file = create_zip(output_dir)
    
    # Provide a download button for the zip file
    st.download_button(
        label="Download All Certificates as ZIP",
        data=zip_file,
        file_name="certificates.zip",
        mime="application/zip"
    )
