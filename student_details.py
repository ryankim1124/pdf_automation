import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from tkinter import Tk, Label, Button, filedialog, messagebox, ttk
from tkinter.font import Font

def create_pdf(row, pdf_file_path):
    try:
        c = canvas.Canvas(pdf_file_path, pagesize=letter)
        width, height = letter

        y = height - 50

        
        c.drawString(100, y, f"Name: {row.get('Name', 'N/A')}")
        y -= 20
        c.drawString(100, y, f"University: {row.get('University', 'N/A')}")
        y -= 20
        c.drawString(100, y, f"Roll Number: {row.get('Roll Number', 'N/A')}")
        y -= 20
        c.drawString(100, y, f"Institute: {row.get('Institute', 'N/A')}")
        y -= 20
        c.drawString(100, y, f"Class: {row.get('Class', 'N/A')}")
        y -= 20
        c.drawString(100, y, f"Company State: {row.get('Company State', 'N/A')}")
        y -= 20
        c.drawString(100, y, f"Company Country: {row.get('Company Country', 'N/A')}")
        y -= 20
        c.drawString(100, y, f"Date of Issuance: {row.get('Date of Issuance', 'N/A')}")
        y -= 20
        c.drawString(100, y, f"Serial Number: {row.get('Serial Number', 'N/A')}")
        y -= 20
        c.drawString(100, y, f"QR URL: {row.get('QR URL', 'N/A')}")

        c.save()
    except Exception as e:
        print(f"Error creating PDF for {row.get('Name', 'Unknown')}: {e}")


def select_excel_file():
    file_path = filedialog.askopenfilename(
        title="Select an Excel file",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    return file_path

def generate_pdfs():
    excel_file_path = select_excel_file()

    if excel_file_path:
        status_label.config(text=f"Selected Excel file: {excel_file_path}")
        try:
          
            student_data = pd.read_excel(excel_file_path)
            total_students = len(student_data)

           
            output_dir = 'student_pdfs'
            os.makedirs(output_dir, exist_ok=True)

            progress_bar["maximum"] = total_students
            progress_bar["value"] = 0

         
            for index, row in student_data.iterrows():
                pdf_file_path = os.path.join(output_dir, f"{row.get('Name', 'student')}_output.pdf")
                create_pdf(row, pdf_file_path)
                progress_bar["value"] += 1
                root.update_idletasks()

           
            messagebox.showinfo("Success", f"PDFs created for all students in {output_dir}.")
        except Exception as e:
            messagebox.showerror("Error", f"Error during PDF creation: {e}")
    else:
        messagebox.showwarning("Warning", "No file selected.")


root = Tk()
root.title("Excel to PDF Generator")
root.geometry("500x400")
root.configure(bg="#f0f0f0")


header_font = Font(family="Helvetica", size=18, weight="bold")
button_font = Font(family="Helvetica", size=12)
label_font = Font(family="Helvetica", size=10)


header_label = Label(root, text="Excel to PDF Generator", font=header_font, bg="#f0f0f0", fg="#333")
header_label.pack(pady=20)

select_button = Button(root, text="Select Excel File and Generate PDFs", font=button_font, command=generate_pdfs, bg="#4CAF50", fg="white", padx=10, pady=5)
select_button.pack(pady=10)

status_label = Label(root, text="Select an Excel file to start.", font=label_font, bg="#f0f0f0", fg="#666")
status_label.pack(pady=10)


progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=20)


footer_label = Label(root, text="Created by Manu and Hithaishi", font=label_font, bg="#f0f0f0", fg="#999")
footer_label.pack(side="bottom", pady=20)


root.mainloop()
