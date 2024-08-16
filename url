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
    
    return filename

# Example usage
url = "http://example.com/qr_codes/student_qr_code_withlink_url.png"
filename = "student_qr_code_with_url.png"

# Generate QR code for the URL
generate_qr_code(url, filename)

print(f"QR code generated and saved as {filename}")
