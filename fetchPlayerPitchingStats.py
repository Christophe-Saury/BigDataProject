import requests

def fetch_data_API1(endpoint_url):
    try:
        response = requests.get(endpoint_url)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))

# Set the parameters
game_type = "'R'"
season = "'2017'"
player_id = "'592789'"

# Construct the endpoint URL
endpoint_url = f"http://lookup-service-prod.mlb.com/json/named.sport_pitching_tm.bam?league_list_id='mlb'&game_type={game_type}&season={season}&player_id={player_id}"

# Fetch the data
data = fetch_data_API1(endpoint_url)

# Print the data
print(data)
