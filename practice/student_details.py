import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_pdf(row, pdf_file_path):
    c = canvas.Canvas(pdf_file_path, pagesize=letter)
    width, height = letter

    y = height - 50

    c.drawString(100, y, f"Name: {row['Name']}")
    y -= 20
    c.drawString(100, y, f"University: {row['University']}")
    y -= 20
    c.drawString(100, y, f"Roll Number: {row['Roll Number']}")
    y -= 20
    c.drawString(100, y, f"Institute: {row['Institute']}")
    y -= 20
    c.drawString(100, y, f"Class: {row['Class']}")
    y -= 20
    c.drawString(100, y, f"Company State: {row['Company State']}")
    y -= 20
    c.drawString(100, y, f"Company Country: {row['Company Country']}")
    y -= 20
    c.drawString(100, y, f"Date of Issuance: {row['Date of Issuance']}")
    y -= 20
    c.drawString(100, y, f"Serial Number: {row['Serial Number']}")
    y -= 20
    c.drawString(100, y, f"QR URL: {row['QR URL']}")

    c.save()


excel_file_path = os.path.join('data', 'Student Dummy Information.xlsx')
print(f"Excel file path: {excel_file_path}")  


student_data = pd.read_excel(excel_file_path)

output_dir = 'student_pdfs'
os.makedirs(output_dir, exist_ok=True)

for index, row in student_data.iterrows():
    pdf_file_path = os.path.join(output_dir, f"{row['Name']}_output.pdf")
    create_pdf(row, pdf_file_path)
    print(f"Created PDF for {row['Name']}: {pdf_file_path}")
