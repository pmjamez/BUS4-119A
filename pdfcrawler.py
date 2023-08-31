import pdfplumber
import re
from webcrawler import pdf_filepath
import os

def find_water_keywords(pdf_path, toc_page_num):
    water_pages = []

    with pdfplumber.open(pdf_path) as pdf:
        toc_page = pdf.pages[toc_page_num - 1]
        toc_text = toc_page.extract_text()

        # Search for the keyword "water" and associated page numbers
        keyword = "water"
        keyword_indices = [m.start() for m in re.finditer(keyword, toc_text, re.IGNORECASE)]
        
        for index in keyword_indices:
            # Extract the page number next to the keyword
            next_space = toc_text.find(' ', index)
            page_number = int(toc_text[index + len(keyword):next_space])
            
            water_pages.append(page_number)

    return water_pages

def navigate_to_water_pages(pdf_path, water_pages):
    water_data = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num in water_pages:
            water_page = pdf.pages[page_num - 1]
            water_text = water_page.extract_text()

            # Apply text extraction techniques to extract water usage information
            
            # Example: Search for numeric values
            water_usage_pattern = re.compile(r'(\d+)\s*(liters|gallons)')
            match = water_usage_pattern.search(water_text)
            
            if match:
                water_value = int(match.group(1))
                water_unit = match.group(2)
                water_data.append({
                    'page_number': page_num,
                    'water_usage': water_value,
                    'unit': water_unit
                })

    return water_data


folder_path = pdf_filepath

# Iterate through the PDF files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(folder_path, filename)

        toc_page_num = 2  # Assuming the TOC is on the second page of each PDF
        water_pages = find_water_keywords(pdf_path, toc_page_num)
        water_data = navigate_to_water_pages(pdf_path, water_pages)

        # Process water data as needed
        print(f"Water data for {filename}:")
        for entry in water_data:
            print(f"Page {entry['page_number']}: {entry['water_usage']} {entry['unit']}")
