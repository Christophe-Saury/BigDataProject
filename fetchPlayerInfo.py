import requests
import json

def fetch_player_info(player_id):
    try:
        endpoint_url = f"http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id='{player_id}'"
        response = requests.get(endpoint_url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))




# Set the player ID
player_id = "493316"

# Fetch player information
data = fetch_player_info(player_id)

print(data)
# Check if data is available
if data is not None:
    # Parse JSON data
    player_info = data['player_info']['queryResults']['row']

    # Extract desired information
    gender = player_info['gender']
    name = player_info['name_display_first_last']
    position = player_info['primary_position_txt']
    age = player_info['age']
    primary_stat_type = player_info['primary_stat_type']
    height_feet = player_info['height_feet']
    height_inches = player_info['height_inches']
    weight = player_info['weight']

    # Format the data
    formatted_data = f"Player ID: {player_id}\nName: {name}\nPosition: {position}\nGender: {gender}\nAge: {age}\nPrimary Stat Type: {primary_stat_type}\nHeight: {height_feet}'{height_inches}\"\nWeight: {weight} lbs"

    # Print the formatted data
    print(formatted_data)
else:
    print("No data fetched from the API.")
