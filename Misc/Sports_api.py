import requests

url = "https://livescore6.p.rapidapi.com/matches/v2/list-live"

querystring = {"Category":"soccer","Timezone":"-7"}

headers = {
	"X-RapidAPI-Key": "f2bb947e8emshbf65478c1438732p159a1djsnaae4183ed02d",
	"X-RapidAPI-Host": "livescore6.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())