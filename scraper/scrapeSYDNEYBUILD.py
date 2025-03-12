from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time
import requests
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException


# Set up the Chrome WebDriver with optimized options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without UI
options.add_argument("--no-sandbox")  # Helps in Linux environments
options.add_argument("--disable-dev-shm-usage")  # Prevents memory issues
options.add_argument("--disable-gpu")  # Optional performance boost
options.add_argument("--blink-settings=imagesEnabled=false")  # Disable images for speed

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)


# Open the exhibitor list page
driver.get("https://www.sydneybuildexpo.com/2025-exhibitors")
time.sleep(5)  # Allow time for elements to load

# Find all exhibitor elements
exhibitors = driver.find_elements(By.CSS_SELECTOR, "a.efp-ehl-items__item")

company_names = []
for exhibitor in exhibitors:
    
    # try:
        # Extract company name
    company_name = exhibitor.find_element(By.CLASS_NAME, "efp-ehl-items__name").text
    
    company_names.append(company_name)


# Close the browser
driver.quit()

company_data = []

# now scrape the website
base_url = 'https://sydneybuild2025.expofp.com/directory.html?'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

for company in company_names:
    try:
        # Format the company name (replace spaces with dashes)
        formatted_company = company.lower().replace(' ', '-')
        
        # Construct the URL
        url = f'{base_url}{formatted_company}'
        # print(url)
        
        driver.get(url)
        
        expo_div = driver.find_element(By.CSS_SELECTOR, "div.expofp-floorplan")
        
        shadow_host = expo_div.find_element(By.XPATH, "./div[not(@class)]")
        
        shadow_root = shadow_host.shadow_root
        
        layout_div = shadow_root.find_element(By.CLASS_NAME, "layout")
        
        layout__fixed_div = layout_div.find_element(By.CLASS_NAME, "layout__fixed")
        
        exhibitor__meta_div = layout__fixed_div.find_element(By.CLASS_NAME, "exhibitor__meta")
        
        links = exhibitor__meta_div.find_elements(By.TAG_NAME, "a")
        
        company_website = None
        
        for link in links:
            href = link.get_attribute("href")
            if href and href.startswith("https://"):
                company_website = href
                break
        
        if company_website:
            company_data.append([company, company_website])
        else:
            company_data.append([company])
            
        print(company, company_website)
       
    except NoSuchElementException as e:
        company_data.append([company])
        print(f"No link for {company}")
    except TimeoutException as e:
        print(f"Error: Timeout occurred while waiting for elements for {company}. Skipping...")
    except WebDriverException as e:
        print(f"Error: WebDriver encountered an issue for {company}: {e}. Skipping...") 
    except Exception as e:
        print(f"An unexpected error occurred for {company}: {e}. Skipping...")    

driver.quit()




def save_to_csv(data):
    with open('../data/sydneybuildexpo.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['Company Name', 'Company Website'])  # Header row
        writer.writerows(data)  # Data rows
        print("done")
        

save_to_csv(company_data)