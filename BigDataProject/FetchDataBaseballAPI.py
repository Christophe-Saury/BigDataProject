import requests

def fetch_data_API1(endpoint_url, params):
    try:
        response = requests.get(endpoint_url, params=params)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))

# Set up authentication if required
api_key = "YOUR_API_KEY"

# Set the endpoint URL and parameters
endpoint_url = "http://lookup-service-prod.mlb.com/json/named.sport_career_hitting.bam"
player_id = "12345"
params = {"league_list_id": "mlb", "game_type": "R", "player_id": player_id}

# Fetch the data
data = fetch_data(endpoint_url, params)

if data is not None:
    stolen_bases = data["sport_career_hitting"]["queryResults"]["row"]
    print(stolen_bases)
    # Process and analyze the stolen base data as needed
else:
    print("Failed to fetch data.")
