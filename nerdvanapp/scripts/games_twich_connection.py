from datetime import datetime
import requests

t = 1459987200

date = datetime.utcfromtimestamp(t).strftime('%Y-%m-%d')

consoles_ids = [169, 167, 130, 6, 49, 48, 12, 9]

url = "https://api.igdb.com/v4/games?fields=name, summary, storyline, platforms, rating, rating_count, first_release_date&offset=0&limit=500"

payload = {}
files = {}
headers = {
  'Client-ID': '3d2zdvuspo8925eerye9r9etrs67dd',
  'Authorization': 'Bearer v4r49hyi6hf9u8147hza6t3tg04qmi',
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload, files=files)

print(response.text)

