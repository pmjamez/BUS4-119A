import os
import pdf2image
import pytesseract

folder_path = "/Users/jamesfolder/Documents/company_pdfs"

# Path to the Tesseract executable (update this based on your system)
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

for filename in os.listdir(folder_path):
        pdf_path = os.path.join(folder_path, filename)
        
        # Convert PDF pages to images using pdf2image
        images = pdf2image.convert_from_path(pdf_path, first_page=1, last_page=1)
    
        if images:
            # Perform OCR on the image
            extracted_text = pytesseract.image_to_string(images[0])
            
            # Print or process the extracted text as needed
            print(f"Text extracted from the first page of '{filename}':\n{extracted_text}")
