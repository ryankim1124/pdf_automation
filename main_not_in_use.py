# import fitz  # PyMuPDF
# import qrcode
# import os
#
# # Function to generate QR code
# def generate_qr_code(data, filename):
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(data)
#     qr.make(fit=True)
#
#     img = qr.make_image(fill_color="black", back_color="white")
#     img.save(filename)
#
# # Function to extract text from PDF
# def extract_text_from_pdf(pdf_file):
#     all_text = ""
#     try:
#         document = fitz.open(pdf_file)
#         for page_num in range(len(document)):
#             page = document.load_page(page_num)
#             all_text += page.get_text() + "\n"
#         document.close()
#     except FileNotFoundError as e:
#         print(f"Error: {e}")
#         return None
#     return all_text
#
# # Function to process PDF and generate QR codes
# def process_pdf_and_generate_qr(pdf_file):
#     text = extract_text_from_pdf(pdf_file)
#     if text is None:
#         print("No text extracted from PDF. Please check the file path.")
#         return
#
#     # Assuming each line in text represents a new QR code
#     lines = text.split('\n')
#     for i, line in enumerate(lines):
#         if line.strip():  # Skip empty lines
#             qr_filename = f"qr_code_{i}.png"
#             generate_qr_code(line.strip(), qr_filename)
#             print(f"Generated QR code for line {i} saved as {qr_filename}")
#
# # Example usage
# def main():
#     pdf_file = r'C:\Users\K Navya sai\Documents\data.pdf'  # Update with your PDF file path
#     if not os.path.exists(pdf_file):
#         print(f"File not found: {pdf_file}")
#         return
#
#     process_pdf_and_generate_qr(pdf_file)
#
#     # Example to read QR code (just for demonstration)
#     # qr_data = read_qr_code('qr_code_0.png')  # Change filename as needed
#     # print("Data from QR code:", qr_data)
#
# if __name__ == "__main__":
#     main()
#
