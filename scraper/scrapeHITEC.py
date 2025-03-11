import requests
from bs4 import BeautifulSoup
from searchCompany import get_first_organic_result  # Import your search function
import csv

# URL of the main exhibitors page
url = 'https://www.hitec.org/exhibits/exhibitors'  # Replace with the actual URL

def scrape_exhibitors(url):
    """Scrape exhibitor names from the main page"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all exhibitor names (adjust the selector based on your page structure)
    exhibitor_elements = soup.find_all('a', {'rel': 'nofollow'})  # Adjust selector based on actual structure
    exhibitor_names = [element.text.strip() for element in exhibitor_elements if element.text.strip()]

    return exhibitor_names


# Step 1: Scrape the exhibitor names from the website
exhibitors = scrape_exhibitors(url)

# Step 2: Use your get_first_organic_result function to find the website for each exhibitor
company_website_data = []

for exhibitor in exhibitors:
    website_url = get_first_organic_result(exhibitor)  # Use your function to get the website
    print(website_url)
    company_website_data.append((exhibitor, website_url))

# Print the results
# for company, website in company_website_data:
#     print(f"Company: {company}, Website: {website}")
    
def save_to_csv(data):
    with open('../data/HITEC.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['Company Name', 'Company Website'])  # Header row
        writer.writerows(data)  # Data rows

save_to_csv(company_website_data)





# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import csv
# import time

# # Set up the Chrome WebDriver with optimized options
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run without UI
# options.add_argument("--no-sandbox")  # Helps in Linux environments
# options.add_argument("--disable-dev-shm-usage")  # Prevents memory issues
# options.add_argument("--disable-gpu")  # Optional performance boost
# options.add_argument("--blink-settings=imagesEnabled=false")  # Disable images for speed

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Function to scrape company data
# def scrape_company_details(url):

#     driver.get(url)
    
#     # Wait for the page to load
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.exhibitors')))

#     exhibitors = driver.find_elements(By.CSS_SELECTOR, 'div.exhibitor')
#     company_details = []


#     for exhibitor in exhibitors:
#         company_name = exhibitor.find_element(By.TAG_NAME, "a").text
        
#         exhibitor.click()
        
#         # Wait for the drawer body to appear
#         WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "drawer-body")))


#         try:
#             website = driver.find_element(By.XPATH, "//a[contains(text(),'Visit website')]")
#             website = website.get_attribute("href")
#         except:
#             website = "No website found"

#         print([company_name, website])
#         company_details.append([company_name, website])

#         # Navigate back
#         driver.back()
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.exhibitors')))

#     return company_details


# def save_to_csv(data):
#     with open('../data/HITEC.csv', mode='w', newline='') as file:
#         writer = csv.writer(file, delimiter=',')
#         writer.writerow(['Company Name', 'Company Website'])  # Header row
#         writer.writerows(data)  # Data rows
#         print("done")
        
# # URL of the main exhibitors page
# url = 'https://www.hitec.org/exhibits/exhibitors'

# # Scrape the data
# company_data = scrape_company_details(url)

# # Print out the data
# # for company in company_data:
# #     print(f"Company Name: {company[0]}, Page: {company[1]}, Website: {company[2]}")

# # save to files
# save_to_csv(company_data)

# # Close the driver
# driver.quit()
