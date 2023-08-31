import os
import fitz  # PyMuPDF

folder_path = "/Users/jamesfolder/Documents/company_pdfs"

def extract_info_above_keyword(text, keyword):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if keyword in line:
            if i > 0:
                return lines[i - 1], line
            else:
                return None, line

    return None, None

for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(folder_path, filename)
        
        # Open the PDF using PyMuPDF
        pdf_document = fitz.open(pdf_path)
        
        # Extract text from all pages

        first_page = pdf_document.load_page(1)
        text = first_page.get_text("")
        
        
        # Close the PDF
        pdf_document.close()

        above_line, water_line = extract_info_above_keyword(text, "Water")
        if above_line is not None:
            print(f"Above Line in '{filename}': {above_line}")
            print(f"Water Line in '{filename}': {water_line}")
        else:
            print(f"Keyword 'Water' not found in '{filename}'")
        
        # Print or process the extracted text as needed
        # print(f"Text extracted from '{filename}':\n{text}")
