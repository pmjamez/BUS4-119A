import selenium
from selenium import webdriver
import os
import pip._vendor.requests
import time

##############
#start of folder creation
desktop_path = os.path.expanduser("~/Documents")
#initializes the path we want into a variable

folder_name = "company_pdfs"
#initializes the folder name into a variable

folder_path = os.path.join(desktop_path, folder_name)

if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    print("Folder Created Successfully")
else:
    print("Folder already exists, writing PDF files now")

###########
# start of web scraper

browser = webdriver.Chrome()

company_names = ["AMD", "TSMC", "Microchip", "Micron"]
# list of company names here

for company_name in company_names:

    search_query = f"{company_name} sustainability report 2023 filetype:pdf"

    browser.get(f"https://www.google.com/search?q={search_query}")

    time.sleep(2)

    try:
         first_result = browser.find_element("css selector", "div.tF2Cxc")
         pdf_link = first_result.find_element("css selector", "a").get_attribute("href")
         print("URL of " + company_name +"'s link:", pdf_link)
    except Exception as e:
         print("Error:", e)

    pdf_response = pip._vendor.requests.get(pdf_link)
    pdf_content = pdf_response.content
    pdf_filename = f"{company_name}_sustainability_report.pdf"
    pdf_filepath = os.path.join(folder_path, pdf_filename)

    with open(pdf_filepath, "wb") as pdf_file:
            pdf_file.write(pdf_content)
    print(f"PDF saved: {pdf_filepath}")

    time.sleep(2)

    # response = pip._vendor.requests.get(pdf_link)
    # pdf_content = response.content

    # with open(folder_name, "wb") as pdf_file:
    #  pdf_file.write(pdf_content)
    #  print(f"PDF saved: {pdf_file}")
 
browser.quit()










