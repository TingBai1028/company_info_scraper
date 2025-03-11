import requests

def get_first_organic_result(query, country="au", page=0, results=10, api_key="67cfcde7d68d1581a845178c"):
    url = "https://api.scrapingdog.com/google/"
    
    # Set up the parameters
    params = {
        "api_key": api_key,
        "query": query,
        "results": results,
        "country": country,
        "page": page
    }

    # Make the request
    response = requests.get(url, params=params)

    # Check the response status
    if response.status_code == 200:
        data = response.json()
        
        # Get the organic results from the response
        organic_results = data.get("organic_results", [])
        
        # If there are results, return the first link
        if organic_results:
            return organic_results[0].get("link")
        else:
            print("No organic results found.")
            return None
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None


# with open("../data/HITEC.csv", mode="a", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
    

#     # Iterate through company names and search for the website
#     for name in company_names:
#         website = get_first_organic_result(name)  # Get website URL from Google
#         writer.writerow([name, website])  # Write company name and website