import selenium
from selenium import webdriver
import requests
import os

driver = webdriver.Chrome()  

company_names = ["AMD", "TSMC", "Microchip"]

pdf_folder = "pdf_reports"
os.makedirs(pdf_folder, exist_ok=True)


for company_name in company_names:
    search_query = f"{company_name} esg report 2023 filetype:pdf"
    
    driver.get(f"https://www.google.com/search?q={search_query}")
    
    search_results = driver.find_elements_by_css_selector("a")
    
    for result in search_results:
        link_url = result.get_attribute("href")
        if link_url and link_url.endswith(".pdf"):
            
            response = requests.get(link_url)
            pdf_path = os.path.join(pdf_folder, f"{company_name}_esg_report_2023.pdf")
            with open(pdf_path, "wb") as pdf_file:
                pdf_file.write(response.content)
            break 
        
driver.quit()

#adding stuff in here


