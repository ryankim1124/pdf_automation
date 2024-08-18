import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="transparent")
    img.save(filename)

# Example usage
student_info = (
    "Name: xxx\n"
    "University: VTU University\n"
    "Roll Number: 123456\n"
    "Institute: EWCE Institute\n"
    "Class: 2024\n"
    "Company Name: Callus\n"
    "Program Start Date: 2024-01-01\n"
    "Program End Date: 2024-12-31\n"
    "Company Address1: 123 Main St\n"
    "Company City:Bengaluru \n"
    "Company State: Karnataka\n"
    "Company Country: India\n"
    "Date of Issuance: 2024-08-09\n"
    "Serial Number: 987654321\n"
    "QR URL: http://example.com/qr"
)

generate_qr_code(student_info, "student_qr_code.png")
