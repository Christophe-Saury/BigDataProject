import requests
import json

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



# Extract relevant values
tbf = int(data['sport_pitching_tm']['queryResults']['row']['tbf'])
hb = int(data['sport_pitching_tm']['queryResults']['row']['hb'])

# Calculate estimated HBP percentage
hbp_percentage = (hb / tbf) * 100

# FIP calculation
era = float(data['sport_pitching_tm']['queryResults']['row']['era'])
k9 = float(data['sport_pitching_tm']['queryResults']['row']['k9'])
bb = int(data['sport_pitching_tm']['queryResults']['row']['bb'])
hr = int(data['sport_pitching_tm']['queryResults']['row']['hr'])
ip = float(data['sport_pitching_tm']['queryResults']['row']['ip'])

fip = ((13 * hr) + (3 * (bb + hbp_percentage / 100)) - (2 * k9)) / ip + 3.2
fip = round(fip, 2)

# Print results





# Extract the top 8 important stats for a pitcher
important_stats = {
    "ERA": data["sport_pitching_tm"]["queryResults"]["row"]["era"],
    "K/9": data["sport_pitching_tm"]["queryResults"]["row"]["k9"],
    "WHIP": data["sport_pitching_tm"]["queryResults"]["row"]["whip"],
    "K/BB": data["sport_pitching_tm"]["queryResults"]["row"]["kbb"],
    "CG": data["sport_pitching_tm"]["queryResults"]["row"]["cg"],
    "SV": data["sport_pitching_tm"]["queryResults"]["row"]["sv"]
}

# calculate fip, war,
# Add FIP to the important_stats dictionary
important_stats["FIP"] = fip


# Create a new JSON object with the selected stats
formatted_json = {
    "player_id": data["sport_pitching_tm"]["queryResults"]["row"]["player_id"],
    "player_name": "Player Name",  # Add player name if available
    "position": "Pitcher",  # Add player position
    "important_stats": important_stats
}

# Convert the formatted JSON object back to a string
formatted_json_str = json.dumps(formatted_json, indent=4)

# Print the formatted JSON string
print(formatted_json_str)