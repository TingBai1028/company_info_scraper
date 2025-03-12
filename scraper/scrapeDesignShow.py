import requests
from bs4 import BeautifulSoup
import csv
import re

# Function to scrape data from the page
def scrape_company_data(url):
    # Send HTTP request to the URL
    response = requests.get(url)
    
    # If the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        company_data = []
        
        # Find company name and website (example of what you may look for)
        company_divs = soup.find_all('div', class_ = 'exhibitor-card style--standard filtered')
        
        
        for company_div in company_divs:
            name_divs = company_div.find('div', class_= 'exhibitor-name')
            company_name = name_divs.get_text(strip=True)
            
            link_divs = company_div.find('div', class_='exhibitor-links')
            
            if link_divs:
                a_tag = link_divs.find('a', class_= 'link-button icon-internet')
                if a_tag:
                    company_website = a_tag['href']
                else:
                    company_website = ''
            else:
                company_website = ''
                
            company_data.append([company_name, company_website])
            print(company_name, company_website)
        
        return company_data

# Function to save the results to a CSV file
def save_to_csv(data):
    with open('../data/designshow.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['Company Name', 'Company Website'])  # Header row
        writer.writerows(data)  # Data rows

# Main function
def main():
    url = 'https://designshow.com.au/exhibitor-list/'  # Replace with the URL you want to scrape
    company_data = scrape_company_data(url)
    # print(company_data);
    
    if company_data:
        save_to_csv(company_data)
        print(f"Data saved to company_info.csv")
    else:
        print("No company data found.")

if __name__ == "__main__":
    main()
