import streamlit as st
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import pdfkit
import os
import zipfile
import io

# Function to generate certificates and reference letters
def generate_certificates_and_reference_letters(uploaded_file, output_dir, template_dir):
    # Read student data from the uploaded Excel file
    student_data = pd.read_excel(uploaded_file)

    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load Jinja2 template environment with custom loader for relative paths
    template_loader = FileSystemLoader(searchpath=template_dir)
    env = Environment(loader=template_loader)

    # Process each student
    for index, student in student_data.iterrows():
        student_info = {
            "Name": student.get("Name", "N/A"),
            "University": student.get("University", "N/A"),
            "RollNumber": student.get("RollNumber", "N/A"),
            "Class": student.get("Class", "N/A"),
            "Institute": student.get("Institute", "N/A"),
            # ... add other fields as required
        }

        try:
            # Generate Certificate PDF using frame_402113.html template
            certificate_template = env.get_template("frame_402113.html")
            rendered_html = certificate_template.render(student_info=student_info)
            certificate_output_file = os.path.join(output_dir, f"{student_info['Name']}_certificate.pdf")
            pdfkit.from_string(rendered_html, certificate_output_file, options={"quiet": True})

            # Generate Reference Letter PDF using letter_of_reference.html template
            reference_letter_template = env.get_template("letter_of_reference.html")
            rendered_html = reference_letter_template.render(student_info=student_info)
            reference_letter_output_file = os.path.join(output_dir, f"{student_info['Name']}_reference_letter.pdf")
            pdfkit.from_string(rendered_html, reference_letter_output_file, options={"quiet": True})

        except Exception as e:
            print(f"Error generating files for {student_info['Name']}: {e}")

    print(f"Certificates and reference letters generated in {output_dir}")

    # Create a ZIP file of the generated PDFs
    zip_file = create_zip(output_dir)

    return zip_file

# Function to create a ZIP file of the generated PDFs
def create_zip(output_dir):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as z:
        for file_name in os.listdir(output_dir):
            if file_name.endswith('.pdf'):
                z.write(os.path.join(output_dir, file_name), file_name)
    zip_buffer.seek(0)
    return zip_buffer

# Main function
def main():
    st.title("Certificate and Reference Letter Generator")

    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:

        # User-friendly prompt to guide path selection
        template_dir = st.text_input("Enter the path to your templates directory:", key="template_dir")
        output_dir = st.text_input("Enter the path to your output directory (where PDFs will be saved):", key="output_dir")

        # Basic input validation (consider expanding based on your needs)
        if not template_dir:
            st.error("Please provide a path to your templates directory.")
            return
        if not output_dir:
            st.error("Please provide a path to your output directory.")
            return

        # Generate the ZIP file
        zip_file = generate_certificates_and_reference_letters(uploaded_file, template_dir, output_dir)

        # Download the generated PDFs as a ZIP file
        st.download_button(
            label="Download All PDFs as ZIP",
            data=zip_file,
            file_name="certificates_and_reference_letters.zip",
            mime="application/zip"
        )

if __name__ == "__main__":
    main()