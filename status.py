import requests
from googlesearch import search

# Open the file containing the domain names
with open("url.txt", "r") as f:
    for line in f:
        # Remove any whitespace characters from the line
        domain_name = line.strip()

        # Use Google search to get the URL of the first search result
        try:
            search_results = search(f"{domain_name}", )
            url = next(search_results)
        except StopIteration:
            print(f"Could not find search result for {domain_name}")
            continue

        # Make a request to the URL using the requests library
        try:
            response = requests.get(url)
            # Print the domain name, its URL, and its HTTP status code
            print(f"{domain_name} ({url}): {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error requesting {url}: {e}")
