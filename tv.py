import requests
import json

# Input the API URL with a placeholder for the query parameter
api_url = 'https://api.tvmaze.com/search/people?q={query}'

# Get user input for the query
user_query = input('Enter your query: ')

# Replace the {query} placeholder with the user's query
api_url = api_url.format(query=user_query)

try:
    # Send an HTTP GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Print the data in JSON format
        print(json.dumps(data, indent=4))
    else:
        print(f"Error: {response.status_code} - {response.text}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
