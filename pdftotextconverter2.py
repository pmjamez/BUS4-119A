import os
import fitz  # PyMuPDF

folder_path = "/Users/jamesfolder/Documents/company_pdfs"

def extract_lines_with_keyword(text, keyword):
    lines = text.split('\n')
    lines_with_keyword = [line for line in lines if keyword in line]
    return lines_with_keyword

for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(folder_path, filename)
        
        # Open the PDF using PyMuPDF
        pdf_document = fitz.open(pdf_path)
        
        # Initialize a list to store lines with "Water" keyword
        water_lines = []
        
        # Iterate through all pages and extract text
        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)
            text = page.get_text("text")

            keyword = "Water"
            
            # Extract lines containing "Water" keyword
            water_lines += extract_lines_with_keyword(text, keyword)
        
        # Close the PDF
        pdf_document.close()
        
        if water_lines:
            print(f"*********Lines with " + keyword +" keyword in '{filename}':* *******")
            for line in water_lines:
                print(line)
        else:
            print(f"No lines with " + keyword + " keyword found in '{filename}'")
