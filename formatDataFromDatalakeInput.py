from pyspark.sql import SparkSession
import json

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# JSON data
data = '''{
    "player_info": {
        "copyRight": "...",
        "queryResults": {
            "totalSize": "1",
            "created": "2023-06-10T08:46:01",
            "row": {
                "college": "",
                "status_date": "2020-10-28T00:00:00",
                "birth_date": "1985-10-18T00:00:00",
                "team_id": "121",
                "active_sw": "N",
                "birth_country": "Cuba",
                "jersey_number": "52",
                "twitter_id": "@ynscspds",
                "name_nick": "La Potencia",
                "name_display_last_first": "Cespedes, Yoenis",
                "primary_position_txt": "LF",
                "name_display_roster_html": "Cespedes",
                "weight": "225",
                "throws": "R",
                "team_name": "New York Mets",
                "death_date": "",
                "name_middle": "",
                "team_abbrev": "NYM",
                "height_feet": "5",
                "status": "Free agent",
                "end_date": "2020-10-29T00:00:00",
                "pro_debut_date": "2012-03-28T00:00:00",
                "birth_city": "Granma",
                "status_code": "FA",
                "gender": "M",
                "name_full": "Cespedes, Yoenis",
                "name_title": "",
                "name_display_first_last": "Yoenis Cespedes",
                "height_inches": "11",
                "name_matrilineal": "Milanes",
                "name_last": "Cespedes",
                "birth_state": "",
                "name_display_last_first_html": "Cespedes, Yoenis",
                "bats": "R",
                "name_prefix": "",
                "player_id": "493316",
                "file_code": "nym",
                "primary_sport_code": "",
                "primary_position": "7",
                "name_display_first_last_html": "Yoenis Cespedes",
                "start_date": "2016-11-30T00:00:00",
                "death_city": "",
                "name_first": "Yoenis",
                "name_use": "Yoenis",
                "death_country": "",
                "high_school": "",
                "team_code": "nyn",
                "death_state": "",
                "name_display_roster": "Cespedes",
                "primary_stat_type": "hitting",
                "age": "37"
            }
        }
    }
}'''

# Parse JSON data
data_dict = json.loads(data)

# Extract player info
player_info = data_dict['player_info']['queryResults']['row']

# Create a DataFrame
df = spark.createDataFrame([player_info])

# Select and format the desired columns
formatted_df = df.selectExpr(
    "player_id AS PlayerID",
    "name_display_first_last AS Name",
    "primary_position_txt AS Position",
    "gender AS Gender",
    "age AS Age",
    "primary_stat_type AS PrimaryStatType",
    "concat(height_feet, \"' \", height_inches, '\"') AS Height",
    "concat(weight, \" lbs\") AS Weight"
)

# Show the formatted data
formatted_df.show(truncate=False)
