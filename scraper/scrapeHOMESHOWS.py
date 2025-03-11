# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import csv
# import time

# # Setup Selenium WebDriver
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run in headless mode (no UI)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Function to scrape exhibitor data from the page
# def scrape_exhibitors(url):
#     driver.get(url)

#     # Wait for the main exhibitor directory element to be visible
#     try:
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, 'div.elementor-element'))
#         )
#     except:
#         print("Error: The main exhibitor content did not load.")
#         driver.quit()
#         return []

#     # Scroll to load all exhibitors (lazy loading)
#     last_height = driver.execute_script("return document.body.scrollHeight")
#     while True:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(3)  # Adjust the time if necessary
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#         last_height = new_height

#     # Find all div elements with exhibitor-title attribute
#     exhibitors = []
#     exhibitor_elements = driver.find_elements(By.CSS_SELECTOR, 'div[exhibitor-title]')

#     if not exhibitor_elements:
#         print("No exhibitor elements found. Check if the selectors are correct.")
#         driver.quit()
#         return []

#     # Extract exhibitor names
#     for exhibitor in exhibitor_elements:
#         exhibitor_title = exhibitor.get_attribute("exhibitor-title")
#         print(exhibitor_title)
#         exhibitors.append([exhibitor_title])

#     return exhibitors

# # Function to save data to CSV
# def save_to_csv(data, filename="exhibitors.csv"):
#     if not data:
#         print("No data to save.")
#         return
    
#     with open(filename, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Exhibitor Title"])  # Column headers
#         writer.writerows(data)
#     print(f"Data saved to {filename}")

# # URL of the exhibitors directory page
# url = "https://homeshows.com.au/sydney/exhibitor-directory/"
# company_data = scrape_exhibitors(url)

# # Save results to CSV
# # save_to_csv(company_data)

# # Close browser
# driver.quit()


# ##########################################################################
# from bs4 import BeautifulSoup
# import csv

# # Function to parse the local HTML file and extract exhibitor names
# def extract_exhibitors_from_html(file_path):
#     with open(file_path, "r", encoding="utf-8") as file:
#         html = file.read()
    
#     soup = BeautifulSoup(html, "html.parser")
    
#     # Modify this selector based on the HTML structure you saved
#     exhibitor_elements = soup.select("p.elementor-heading-title a")
    
#     exhibitors = []
#     for exhibitor in exhibitor_elements:
#         exhibitor_name = exhibitor.text.strip()  # Get the name and strip any extra spaces
#         # print(exhibitor_name)
#         exhibitors.append([exhibitor_name])

#     return exhibitors



# ####### extract url

# # Load the local HTML file
# with open("homeshow.html", "r", encoding="utf-8") as file:
#     soup = BeautifulSoup(file, "html.parser")

# # Find the <a> tags inside the structure you mentioned
# links = soup.select('div.elementor-widget-container p.elementor-heading-title a[href]')

# # Extract and print the URLs
# urls = [link['href'] for link in links]



# ####### go into url and extract data
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# # Setup Selenium WebDriver
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run in headless mode (no UI)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Function to scrape data from company website
# def extract_website_link(url):
#     driver.get(url)
    
#     # Wait for the page to load fully
#     time.sleep(3)  # Adjust the time if necessary or use WebDriverWait to wait for a specific element
    
#     try:
#         # Find the 'Website' link
#         website_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div[5]/div/div/a")
#         website_link = website_button.get_attribute("href")
#         return website_link
#     except:
#         print(f"Could not find the 'Website' link for {url}")
#         return None

# # Loop through all company links and scrape the data
# for url in urls:
#     extract_website_link(url)

# # Close the browser
# driver.quit()


# # Function to save extracted data to a CSV file
# def save_to_csv(data, filename="exhibitors.csv"):
#     if not data:
#         print("No data to save.")
#         return
    
#     with open(filename, mode="w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Exhibitor Name"])  # Column headers
#         writer.writerows(data)
#     print(f"Data saved to {filename}")

# # Path to your local HTML file
# file_path = "./homeshow.html"  # Replace this with the correct path if needed
# company_data = extract_exhibitors_from_html(file_path)

# # Save the extracted data to CSV
# # save_to_csv(company_data)

###############################################################
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Function to parse the local HTML file and extract exhibitor names
def extract_exhibitors_from_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        html = file.read()
    
    soup = BeautifulSoup(html, "html.parser")
    
    # Modify this selector based on the HTML structure you saved
    exhibitor_elements = soup.select("p.elementor-heading-title a")
    
    exhibitors = []
    for exhibitor in exhibitor_elements:
        exhibitor_name = exhibitor.text.strip()  # Get the name and strip any extra spaces
        exhibitors.append([exhibitor_name])

    return exhibitors

# Load the local HTML file
with open("homeshow.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Find the <a> tags inside the structure you mentioned
links = soup.select('div.elementor-widget-container p.elementor-heading-title a[href]')

# Extract and print the URLs
urls = [link['href'] for link in links]

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no UI)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# List to store company names and website links
company_data = []

# Function to scrape data from company website
def extract_website_link(url, exhibitor_name):
    driver.get(url)
    
    # Wait for the page to load fully
    time.sleep(3)  # Adjust the time if necessary or use WebDriverWait to wait for a specific element
    
    try:
        # Find the 'Website' link
        website_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div[5]/div/div/a")
        website_link = website_button.get_attribute("href")
        print(f"Found: {exhibitor_name} - {website_link}")
    except:
        website_link = None
        print(f"Could not find the 'Website' link for {url}")
    
    company_data.append([exhibitor_name, website_link])  # Store the name and link in the list

# Loop through all company links and scrape the data
for exhibitor, url in zip(extract_exhibitors_from_html("homeshow.html"), urls):
    extract_website_link(url, exhibitor[0])  # Pass company name and URL

# Close the browser
driver.quit()


# Save the data into a CSV file
with open('../data/homeshows.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Company Name', 'Company Website'])  # Write the header
    writer.writerows(company_data)  # Write the company data

print("Data saved to 'exhibitors_data.csv'")
