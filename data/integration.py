import cv2
from pyzbar.pyzbar import decode

def read_qr_code(qr_image):
    img = cv2.imread(qr_image)
    detected_barcodes = decode(img)

    for barcode in detected_barcodes:
        if barcode.data:
            return barcode.data.decode('utf-8')
    return None