from selenium import webdriver
import os
import pip._vendor.requests
import time
import fitz


desktop_path = os.path.expanduser("~/Documents")

folder_name = "company_pdfs"
#initializes the folder name into a variable

folder_path = os.path.join(desktop_path, folder_name)

if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    print("Folder Created Successfully")
else:
    print("Folder already exists, writing PDF files now")

def is_pdf_corrupted(pdf_filepath):
     try:
        pdf_document = fitz.open(pdf_filepath)
        time.sleep(2)
        num_pages = pdf_document.page_count
        return num_pages > 0
     except Exception as e:
        return False
    

###########
# start of web scraper

browser = webdriver.Chrome()

def searcher1(company_name):

    search_query = f"{company_name} sustainability report 2023 filetype:pdf"
    browser.get(f"https://www.google.com/search?q={search_query}")

    try:
         first_result = browser.find_element("css selector", "div.tF2Cxc")
         pdf_link = first_result.find_element("css selector", "a").get_attribute("href")
         print("URL of " + company_name +"'s link:")
    except Exception as e:
         print("Error:", e)

    time.sleep(3)
    print("0")
    pdf_response = pip._vendor.requests.get(pdf_link)
    print("1")
    time.sleep(3)
    pdf_content = pdf_response.content
    print("12")
    pdf_filename = f"{company_name}_report1.pdf"
    print("123")
    pdf_filepath = os.path.join(folder_path, pdf_filename)
    print("1234")

    time.sleep(1)

    with open(pdf_filepath, "wb") as pdf_file:
            print("creating file")
            
            pdf_file.write(pdf_content)
    
    return pdf_filepath

def searcher2(company_name):

    search_query = f"{company_name} Corporate Responsibility report 2023 filetype:pdf"
    browser.get(f"https://www.google.com/search?q={search_query}")

    try:
         first_result = browser.find_element("css selector", "div.tF2Cxc")
         pdf_link = first_result.find_element("css selector", "a").get_attribute("href")
         print("URL of " + company_name +"'s link:")
    except Exception as e:
         print("Error:", e)

    time.sleep(3)

    pdf_response = pip._vendor.requests.get(pdf_link)
    time.sleep(3)
    pdf_content = pdf_response.content
    pdf_filename = f"{company_name}_report2.pdf"
    pdf_filepath = os.path.join(folder_path, pdf_filename)

    time.sleep(1)

    with open(pdf_filepath, "wb") as pdf_file:
            print("creating file")
            
            pdf_file.write(pdf_content)
    
    return pdf_filepath

def searcher3(company_name):

    search_query = f"{company_name}  2023 filetype:pdf"
    browser.get(f"https://www.google.com/search?q={search_query}")

    try:
         first_result = browser.find_element("css selector", "div.tF2Cxc")
         pdf_link = first_result.find_element("css selector", "a").get_attribute("href")
         print("URL of " + company_name +"'s link:")
    except Exception as e:
         print("Error:", e)

    time.sleep(3)

    pdf_response = pip._vendor.requests.get(pdf_link)
    time.sleep(3)
    pdf_content = pdf_response.content
    pdf_filename = f"{company_name}_report3.pdf"
    pdf_filepath = os.path.join(folder_path, pdf_filename)

    time.sleep(1)

    with open(pdf_filepath, "wb") as pdf_file:
            print("creating file")
            
            pdf_file.write(pdf_content)
    
    return pdf_filepath
    
company_names = ["AMD", "TSMC", "Microchip", "Micron"]
# list of company names here

for company_name in company_names:

    pdf_filepaths = [searcher1(company_name), searcher2(company_name), searcher3(company_name)]

    for pdf_filepath in pdf_filepaths:
          if is_pdf_corrupted(pdf_filepath):
             print("The PDF is not corrupted.")
          else:
             print("The PDF is corrupted.")
             os.remove(pdf_filepath)
             print("File has been deleted")
             continue

          pdf_document = fitz.open(pdf_filepath)
          num_pages = pdf_document.page_count

          if num_pages < 10:
             os.remove(pdf_filepath)
             print("File too small")
         
   


   

    # time.sleep(5)
    # page_reader = PyPDF2.PdfFileReader(pdf_file)
    # num_pages = page_reader.getNumPages()

    

    print(f"PDF saved and # of pages: {num_pages}")


   
browser.quit()










