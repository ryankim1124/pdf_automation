from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Student Certificate', 0, 1, 'C')

    def student_details(self, details):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, details)
        self.ln(10)

    def qr_code(self, qr_image):
        self.image(qr_image, x=10, y=60, w=50)