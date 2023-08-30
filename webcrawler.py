import selenium
from selenium import webdriver
import os

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


browser = webdriver.Chrome()

company_names = ["AMD, TSMC"]
# list of company names here

for company_name in company_names:
    search_query = f"{company_name} sustainability report 2023 filetype:pdf"
    






