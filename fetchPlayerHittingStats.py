import requests

def fetch_data_API1(endpoint_url, params=None):
    try:
        response = requests.get(endpoint_url, params=params)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))

# Set the endpoint URL
endpoint_url = "http://lookup-service-prod.mlb.com/json/named.sport_career_hitting.bam"

# Set the parameters
params = {
    "league_list_id": "mlb",
    "game_type": "R",
    "player_id": "493316"
}

# Fetch the data
data = fetch_data_API1(endpoint_url, params=params)

# Print the data
print(data)
