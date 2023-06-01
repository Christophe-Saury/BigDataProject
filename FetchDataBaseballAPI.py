
import requests

# Set up authentication if required
api_key = "YOUR_API_KEY"

# Set the endpoint URL and parameters
endpoint_url = "http://lookup-service-prod.mlb.com/json/named.sport_career_hitting.bam?league_list_id='mlb'&game_type='R'&player_id='493316'"
player_id = "12345"
params = {"playerId": player_id, "statType": "stolenBase"}

# Make the HTTP request

response = requests.get(endpoint_url)

# Handle the response
if response.status_code == 200:
    data = response.json()
    stolen_bases = data
    print (stolen_bases)
    # Process and analyze the stolen base data as needed
else:
    print("Error:", response.status_code)
