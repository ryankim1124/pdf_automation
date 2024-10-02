from flask import Flask, render_template
import openpyxl
import qrcode

app = Flask(__name__)

@app.route('/')
def generate_qr_codes():
    # Read data from Excel
    workbook = openpyxl.load_workbook('your_excel_file.xlsx')
    sheet = workbook.active
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)

    # Generate QR codes
    qr_codes = []
    for row in data:
        qr = qrcode.make(row[0])  # Assuming the first column contains QR code data
        qr_codes.append(qr)

    return render_template('your_template.html', data=data, qr_codes=qr_codes)

if __name__ == '__main__':
    app.run()