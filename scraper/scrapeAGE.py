
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv

# Set up the Chrome WebDriver with optimized options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without UI
options.add_argument("--no-sandbox")  # Helps in Linux environments
options.add_argument("--disable-dev-shm-usage")  # Prevents memory issues
options.add_argument("--disable-gpu")  # Optional performance boost
options.add_argument("--blink-settings=imagesEnabled=false")  # Disable images for speed

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Function to scrape company data
def scrape_company_details(url):
    driver.get(url)
    
    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.exhibitors__item')))

    exhibitors = driver.find_elements(By.CSS_SELECTOR, 'div.exhibitors__item')
    company_details = []

    for exhibitor in exhibitors:
        company_name = exhibitor.get_attribute('title')
        
        # Get the link without clicking
        link = exhibitor.find_element(By.TAG_NAME, 'a').get_attribute('href')

        # Open the company details page
        driver.get(link)

        try:
            # Wait for the company details page to load
            website = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'li.info__item a'))
            ).get_attribute('href')
        except:
            website = "No website found"

        company_details.append([company_name, website])

        # Navigate back
        driver.back()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.exhibitors__item')))

    return company_details


def save_to_csv(data):
    with open('../data/AGE.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['Company Name', 'Company Website'])  # Header row
        writer.writerows(data)  # Data rows
        print("done")
        
# URL of the main exhibitors page
url = 'https://austgamingexpo.com/exhibitors/'

# Scrape the data
company_data = scrape_company_details(url)

# Print out the data
# for company in company_data:
#     print(f"Company Name: {company[0]}, Page: {company[1]}, Website: {company[2]}")

# save to files
save_to_csv(company_data)

# Close the driver
driver.quit()
