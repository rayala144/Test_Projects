import requests

download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
target_csv_path = "Pandas/Dataset_explore/nba_all_elo.csv" 

response = requests.get(download_url)
response.raise_for_status()

with open(target_csv_path, "wb") as target:
    target.write(response.content)
print("Download complete")