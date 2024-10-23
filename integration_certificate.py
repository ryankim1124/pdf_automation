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

    # Load Jinja2 template environment
    env = Environment(loader=FileSystemLoader(template_dir))

    # Process each student
    for index, student in student_data.iterrows():
        student_info = {
            "Name": student.get("Name", "N/A"),
            "University": student.get("University", "N/A"),
            # ... add other fields as required
        }

        try:
            # Generate Certificate PDF
            certificate_output_file = os.path.join(output_dir, f"{student_info['Name']}_certificate.pdf")
            template = env.get_template("frame_402113.html")
            rendered_html = template.render(student_info=student_info)
            pdfkit.from_string(rendered_html, certificate_output_file)

            # Generate Reference Letter PDF
            reference_letter_output_file = os.path.join(output_dir, f"{student_info['Name']}_reference_letter.pdf")
            template = env.get_template("letter_of_reference.html")
            rendered_html = template.render(student_info=student_info)
            pdfkit.from_string(rendered_html, reference_letter_output_file)
        except Exception as e:
            print(f"Error generating files for {student_info['Name']}: {e}")

    print(f"Certificates and reference letters generated in {output_dir}")

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
        # Specify paths
        template_dir = "C:\\Users\\K Navya sai\\OneDrive\\Desktop\\internship\\pdf_automation\\data\\templates\\pages"
        output_dir = os.path.join("C:\\Users\\K Navya sai\\OneDrive\\Desktop\\internship\\pdf_automation", "generated_pdfs")
        
        generate_certificates_and_reference_letters(uploaded_file, output_dir, template_dir)

        st.success("Certificates and reference letters generated successfully!")

        zip_file = create_zip(output_dir)
        st.download_button(
            label="Download All PDFs as ZIP",
            data=zip_file,
            file_name="certificates_and_reference_letters.zip",
            mime="application/zip"
        )

if __name__ == "__main__":
    main()
