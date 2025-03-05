import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape data from the page
def scrape_company_data(url):
    # Send HTTP request to the URL
    response = requests.get(url)
    
    # If the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        company_data = []
        
        # Find company name and website (example of what you may look for)
        company_divs = soup.find_all('div', class_ = 'et_pb_toggle')
        
        for company_div in company_divs:
            company_name_tag = company_div.find('h5', class_ = 'et_pb_toggle_title')
            if company_name_tag:
                company_name = company_name_tag.get_text(strip=True) # company name
                # print(company_name)
                website_div = company_div.find('div', class_='et_pb_toggle_content clearfix')
                if website_div:
                    a_tag = website_div.find('a')
                    if a_tag:
                        company_website = a_tag['href']
                        # print(company_website)
                        company_data.append([company_name, company_website])
        
        return company_data

# Function to save the results to a CSV file
def save_to_csv(data):
    with open('data/companies.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Company Name', 'Company Website'])  # Header row
        writer.writerows(data)  # Data rows

# Main function
def main():
    url = 'https://ahiceconference.com/asiapacific/exhibitors/'  # Replace with the URL you want to scrape
    company_data = scrape_company_data(url)
    # print(company_data);
    
    if company_data:
        save_to_csv(company_data)
        print(f"Data saved to company_info.csv")
    else:
        print("No company data found.")

if __name__ == "__main__":
    main()
