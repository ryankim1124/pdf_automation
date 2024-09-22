# app.py
from flask import Flask, render_template, send_file
import qrcode
import io

app = Flask(__name__)

# Route to render the HTML page
@app.route('/')
def home():
    return render_template('index.html')  # Ensure you have an index.html in the templates folder

# Route to generate and display QR code
@app.route('/generate_qr')
def generate_qr():
    # Sample data for QR code
    data = "Sample data for QR code"
    
    # Generate QR code
    qr = qrcode.make(data)
    qr_io = io.BytesIO()
    qr.save(qr_io, 'PNG')
    qr_io.seek(0)

    return send_file(qr_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

