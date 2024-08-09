import pandas as pd
import os
def read_excel_file(file_path):
    """
    Reads an Excel file and extracts student information.

    :param file_path: Path to the Excel file.
    :return: DataFrame containing the Excel data.
    """
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        return df
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None
def process_student_info(df):
    """
    Processes student information from the DataFrame.

    :param df: DataFrame containing the student information.
    :return: List of dictionaries with student information.
    """
    try:
        student_info = df.to_dict(orient='records')
        return student_info
    except Exception as e:
        print(f"Error processing student information: {e}")
        return None
def display_student_info(student_info):
    """
    Displays student information.

    :param student_info: List of dictionaries with student information.
    """
    for student in student_info:
        print(f"Student Name: {student.get('Name')}")
        print(f"University: {student.get('University')}")
        print(f"Roll Number: {student.get('Roll Number')}")
        print(f"Institute: {student.get('Institute')}")
        print(f"Class: {student.get('Class')}")
        print(f"Company Name: {student.get('Company Name')}")
        print(f"Program Start Date: {student.get('Program Start Date')}")
        print(f"Program End Date: {student.get('Program End Date')}")
        print(f"Company Address1: {student.get('Company Address1')}")
        print(f"Company Address2: {student.get('Company Address2')}")
        print(f"Company City: {student.get('Company City')}")
        print(f"Company State: {student.get('Company State')}")
        print(f"Company Country: {student.get('Company Country')}")
        print(f"Date of Issuance: {student.get('Date of Issuance')}")
        print(f"Serial Number: {student.get('Serial Number')}")
        print(f"QR URL: {student.get('QR URL')}")
        
        print("")
def main(file_path):
    """
    Main function to execute the Excel information extraction.

    :param file_path: Path to the Excel file.
    """
    df = read_excel_file(file_path)
    if df is not None:
        
        student_info = process_student_info(df)
        if student_info is not None:
            
            display_student_info(student_info)

if __name__ == "__main__":
    
    excel_file_path = r"C:\Users\manuk\OneDrive\Desktop\callus_project\pdf_automation\data\Student Dummy Information.xlsx"
    main(excel_file_path)
   
if os.path.isfile(excel_file_path):
    print(f"File found: {excel_file_path}")
else:
    print(f"File not found: {excel_file_path}")
