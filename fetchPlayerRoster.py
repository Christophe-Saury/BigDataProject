import requests
import json

def fetch_roster_data(team_id):
    try:
        endpoint_url = f"http://lookup-service-prod.mlb.com/json/named.roster_40.bam?team_id='{team_id}'"
        response = requests.get(endpoint_url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))

# Set the team ID
team_id = "121"

# Fetch roster data
data = fetch_roster_data(team_id)

# Check if data is available
if data is not None:
    # Parse JSON data
    roster = data['roster_40']['queryResults']['row']

    # Extract desired information
    team_name = roster[0]['team_full']
    players = roster[1:]

    # Print team name
    print("Team Name:", team_name)

    # Print player information
    print("Player Roster:")
    for player in players:
        player_id = player['player_id']
        player_name = player['name_display_first_last']
        position = player['position_txt']
        jersey_number = player['jersey_number']

        print(f"Player ID: {player_id}, Name: {player_name}, Position: {position}, Jersey Number: {jersey_number}")
else:
    print("No data fetched from the API.")
