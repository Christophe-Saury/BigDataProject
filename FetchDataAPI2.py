import requests

url = "https://mlb-data.p.rapidapi.com/json/named.player_teams.bam"

querystring = {"player_id":"'493316'","season":"'2014'"}

headers = {
	"X-RapidAPI-Key": "2b07d62678msh94780def3be43cdp1f4712jsn9e951d16e2d7",
	"X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())