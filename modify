import qrcode
import os

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create the image with black QR code on a transparent background
    img = qr.make_image(fill_color="black", back_color="transparent")
    img.save(filename)
    
    return filename

def generate_qr_url(base_url, filename):
    # Generate the full QR URL based on the filename
    return f"{base_url}/{filename}"

# Example usage
filename = "student_qr_code.png"
base_url = "http://example.com/qr_codes"

student_info = (
    "Name: sai\n"
    "University: XYZ University\n"
    "Roll Number: 123456\n"
    "Institute: ABC Institute\n"
    "Class: 2024\n"
    "Company Name: DEF Corporation\n"
    "Program Start Date: 2024-01-01\n"
    "Program End Date: 2024-12-31\n"
    "Company Address1: 123 Main St\n"
    "Company City: Banglore\n"
    "Company State: Karnataka\n"
    "Company Country: India\n"
    "Date of Issuance: 2024-08-09\n"
    "Serial Number: 987654321\n"
)

# Generate the QR code
generate_qr_code(student_info, filename)

# Generate the QR URL and append it to student_info
qr_url = generate_qr_url(base_url, filename)
student_info += f"\nQR URL: {qr_url}"

# Generate the final QR code with all details including the QR URL
final_filename = "student_qr_code_with_url.png"
generate_qr_code(student_info, final_filename)

print(f"QR code generated and saved as {final_filename}")
