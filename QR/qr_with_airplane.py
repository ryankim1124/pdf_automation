import qrcode
from PIL import Image

def generate_qr_code_with_airplane(data, base_url, filename, icon_path):
  """
  Generates a QR code with a peach background and an airplane symbol, and saves it to the specified file.
  """

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

  # Generate the image with a peach background
  img = qr.make_image(fill_color="black", back_color=(255, 218, 185))  # RGB for a light peach color

  # Load the airplane icon from the Downloads folder
  icon = Image.open("data\\template\\assets\\images\\airplane_screenshot.png") 

  # Resize the icon to fit the QR code
  icon_size = 40
  icon = icon.resize((icon_size, icon_size))

  # Calculate the position to center the icon on the QR code
  img_width, img_height = img.size
  icon_x = (img_width - icon_size) // 2
  icon_y = (img_height - icon_size) // 2

  # Paste the icon onto the QR code
  img.paste(icon, (icon_x, icon_y), icon)

  # Save the QR code
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
generate_qr_code_with_airplane(student_info, base_url, "student_qr_code_with_airplane.png", "C:\\Users\\K Navya sai\\Downloads\\airplane.png")