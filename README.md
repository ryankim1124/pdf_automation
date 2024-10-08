# pdf_automation
PDF automation for letter of reference and certificate of internship based on the excel data.

### Running the Project
1. Clone the repository: `git clone https://github.com/ryankim1124/pdf_automation`
2. Navigate to the directory: `cd project`

#  Certificate Generator

This application allows users to generate PDF certificates for students based on their information stored in an Excel file. The application is built using Streamlit, which creates an interactive web interface for generating certificates easily.

## Features

- Upload an Excel file containing student details.
- Automatically generate PDF certificates for each student.
- Download all generated certificates in a user-friendly manner.

## Requirements

Make sure you have the following packages installed:

- Python 3.x
- Streamlit
- Pandas
- ReportLab
- OpenPyXL

You can install the required packages using pip:

```bash
pip install streamlit pandas reportlab openpyxl

### Example
```bash
$ streamlit run student_details.py
Processing...
Certificate generated successfully!
