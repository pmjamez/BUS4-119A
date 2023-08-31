import os
import io
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

def extract_text_from_first_page(pdf_path):
    resource_manager = PDFResourceManager()
    output_stream = io.StringIO()
    laparams = LAParams()

    with open(pdf_path, 'rb') as pdf_file:
        device = TextConverter(resource_manager, output_stream, laparams=laparams)
        interpreter = PDFPageInterpreter(resource_manager, device)
        
        for page in PDFPage.get_pages(pdf_file, set(), maxpages=1, caching=True):
            interpreter.process_page(page)
            
        text = output_stream.getvalue()

    return text


folder_path = "/Users/jamesfolder/Documents/company_pdfs"

for filename in os.listdir(folder_path):
    pdf_path = os.path.join(folder_path, filename)
    print(pdf_path)

    title_name = extract_text_from_first_page(pdf_path)
    print(title_name)

# def find_water_keywords(pdf_path, toc_page_num):
#     water_pages = []

#     with pdfplumber.open(pdf_path) as pdf:
#         toc_page = pdf.pages[toc_page_num - 1]
#         toc_text = toc_page.extract_text()

#         pattern = re.compile(r'(\d+)\s*water', re.IGNORECASE)
#         matches = pattern.findall(toc_text)
        
#         water_pages = [int(match) for match in matches]

#     print(water_pages)
#     return water_pages


# def navigate_to_water_pages(pdf_path, water_pages):
#     water_data = 0

#     with pdfplumber.open(pdf_path) as pdf:
#         for page_num in water_pages:
#             water_page = pdf.pages[page_num - 1]
#             water_text = water_page.extract_text()

            
#             water_usage_pattern = re.compile(r'(\d+)\s*(liters|gallons)')
#             match = water_usage_pattern.search(water_text)
            
#             if match:
#                 water_value = int(match.group(1))
#                 water_unit = match.group(2)
#                 water_data.append({
#                     'page_number': page_num,
#                     'water_usage': water_value,
#                     'unit': water_unit
#                 })

#     return water_data



    #toc_page_num = 2  
    
   

# # Iterate through the PDF files in the folder
# for filename in os.listdir(folder_path):
#     pdf_path = os.path.join(folder_path, filename)

#     toc_page_num = 2  # Assuming the TOC is on the second page of each PDF
#     water_pages = find_water_keywords(pdf_path, toc_page_num)
#     water_data = navigate_to_water_pages(pdf_path, water_pages)

#     # Process water data as needed
#     print(f"Water data for {filename}:")
#     for entry in water_data:
#          print(f"Page {entry['page_number']}: {entry['water_usage']} {entry['unit']}")
