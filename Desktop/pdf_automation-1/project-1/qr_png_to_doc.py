from fpdf import FPDF

# Create a PDF document
pdf = FPDF()
pdf.add_page()

# Add the QR code image to the PDF
pdf.image("student_qr_code.png", x=10, y=10, w=100)  # Adjust the position and size

# Save the output as a PDF file
pdf.output("qr_code_document.pdf")
