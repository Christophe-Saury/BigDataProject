import requests
from pyspark.sql import SparkSession

def fetch_data_API1(endpoint_url):
    try:
        response = requests.get(endpoint_url)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))

# Set up authentication if required
api_key = "YOUR_API_KEY"

# Set the endpoint URL and parameters
endpoint_url = "http://lookup-service-prod.mlb.com/json/named.sport_career_hitting.bam?league_list_id='mlb'&game_type='R'&player_id='493316'"
player_id = "12345"
params = {"league_list_id": "mlb", "game_type": "R", "player_id": player_id}

# Fetch the data
data = fetch_data_API1(endpoint_url)


print(data)
    # Process and analyze the stolen base data as needed




# Create a SparkSession
spark = SparkSession.builder \
    .appName("MLB DataLake") \
    .getOrCreate()

# Convert the data to a Spark DataFrame
df = spark.createDataFrame(data["sport_career_hitting"]["queryResults"]["row"])

# Define the path to save the data in your DataLake
output_path = "s3://your-bucket-name/path/to/save/data"

# Save the DataFrame to your DataLake
df.write.mode("overwrite").parquet(output_path)

# Alternatively, you can save the DataFrame as other formats such as CSV, JSON, etc.
# df.write.mode("overwrite").csv(output_path)
# df.write.mode("overwrite").json(output_path)

# Stop the SparkSession
spark.stop()
