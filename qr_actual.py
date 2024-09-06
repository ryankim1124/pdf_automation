import qrcode

def generate_qr_code(data, base_url, filename):
    # Concatenate the base URL with the student-specific data
    full_url = f"{base_url}"

    # Create the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(full_url)
    qr.make(fit=True)

    # Generate the image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Example usage
student_info = {
    "name": "xxx",
    "university": "VTU University",
    "roll_number": "123456",
    "institute": "EWCE Institute",
    "class": "2024",
    "company_name": "Callus",
    "program_start_date": "2024-01-01",
    "program_end_date": "2024-12-31",
    "company_address1": "123 Main St",
    "company_city": "Bengaluru",
    "company_state": "Karnataka",
    "company_country": "India",
    "date_of_issuance": "2024-08-09",
    "serial_number": "987654321",
}

base_url = "https://sprint.calluscompany.com/certificate/clyxchj430001dfl4dijb9v9g"
generate_qr_code(student_info, base_url, "student_qr_code.png")

