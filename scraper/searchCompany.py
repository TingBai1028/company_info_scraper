# import requests

# api_key = "67cf713ba8e1e65ac841a551"
# url = "https://api.scrapingdog.com/google/"

# params = {
#     "api_key": api_key,
#     "query": "ARBV Architects Registration Board of Victoria",
#     "results": 10,
#     "country": "au",
#     "page": 0
# }

# response = requests.get(url, params=params)

# if response.status_code == 200:
#     data = response.json()
    
#     organic_results = data.get("organic_results", [])
#     link = organic_results[0].get("link")
    
#     print(link)
# else:
#     print(f"Request failed with status code: {response.status_code}")

import requests

def get_first_organic_result(query, country="au", page=0, results=10, api_key="67cf713ba8e1e65ac841a551"):
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

