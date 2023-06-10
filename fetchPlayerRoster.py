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



# Extract player IDs of pitchers
pitcher_ids = []
pitchers = data['roster_40']['queryResults']['row']
for pitcher in pitchers:
    if pitcher['position_txt'] == 'P':
        pitcher_ids.append(pitcher['player_id'])

i = 0

# Print the pitcher IDs
for pitcher_id in pitcher_ids:
  
    i=i+1
print (i)

print(pitcher_ids)






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
pitcher_ids = ['493316','656257', '676130', '471911', '595928', '488984', '608678', '664192', '656731', '669105', '657697', '668665', '493603', '656849', '548384', '660593', '502085', '453286', '673540', '622098', '670955', '434378', '677020']

# Initialize a dictionary to store the accumulated stats
accumulated_stats = {
    "ERA": [],
    "K/9": [],
    "WHIP": [],
    "K/BB": [],
    "CG": [],
    "SV": []
}

# Iterate over each pitcher ID
for pitcher_id in pitcher_ids:
    # Construct the endpoint URL
    endpoint_url = f"http://lookup-service-prod.mlb.com/json/named.sport_pitching_tm.bam?league_list_id='mlb'&game_type={game_type}&season={season}&player_id='{pitcher_id}'"

    # Fetch the data
    data = fetch_data_API1(endpoint_url)

    # Check if the data dictionary contains the expected keys
    if "sport_pitching_tm" in data and "queryResults" in data["sport_pitching_tm"]:
        query_results = data["sport_pitching_tm"]["queryResults"]

        # Check if the queryResults dictionary contains at least one row
        if "row" in query_results and isinstance(query_results["row"], dict):
            row = query_results["row"]

            # Extract the important stats
            important_stats = {
                "ERA": float(row["era"]),
                "K/9": float(row["k9"]),
                "WHIP": float(row["whip"]),
                "K/BB": float(row["kbb"]),
                "CG": int(row["cg"]),
                "SV": int(row["sv"])
            }

            # Append the stats to the accumulated_stats list
            for stat in accumulated_stats:
                accumulated_stats[stat].append(important_stats[stat])
        else:
            print("No row found in queryResults.")
    else:
        print("Invalid data format.")
        
        
# Calculate the average of the accumulated stats
average_stats = {}
for stat in accumulated_stats:
    stat_list = accumulated_stats[stat]
    if stat_list:
        average_stats[stat] = round(sum(stat_list) / len(stat_list), 2)
    else:
        average_stats[stat] = 0

# Calculate FIP using the average stats
HR = average_stats["HR"] if "HR" in average_stats else 0
BB = average_stats["BB"] if "BB" in average_stats else 0
HBP = average_stats["HBP"] if "HBP" in average_stats else 0
K = average_stats["K"] if "K" in average_stats else 0
IP = average_stats["IP"] if "IP" in average_stats and average_stats["IP"] != 0 else 1
constant = 3.2  # Adjust the constant value based on league average

FIP = ((13 * HR) + (3 * (BB + HBP)) - (2 * K)) / IP + constant
average_stats["FIP"] = round(FIP, 2)

# Create a new JSON object with the average stats
formatted_json = {
    "average_stats": average_stats
}

# Convert the formatted JSON object back to a string
formatted_json_str = json.dumps(formatted_json, indent=4)

# Print the formatted JSON string
print(formatted_json_str)