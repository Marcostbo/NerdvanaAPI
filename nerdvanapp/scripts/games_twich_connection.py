from datetime import datetime
import requests
import copy

t = 1459987200

date = datetime.utcfromtimestamp(t).strftime('%Y-%m-%d')

consoles_ids = [169, 167, 130, 6, 49, 48, 12, 9]

payload = {}
files = {}
headers = {
  'Client-ID': '3d2zdvuspo8925eerye9r9etrs67dd',
  'Authorization': 'Bearer v4r49hyi6hf9u8147hza6t3tg04qmi',
  'Accept': 'application/json'
}

full_games = []
stop = 0
limit = 500
offset = 0

while stop == 0:

    url = f"https://api.igdb.com/v4/games" \
          f"?fields=name,%20summary,%20storyline,%20platforms,%20rating,%20rating_count,%20first_release_date," \
          f"%20involved_companies,%20category&limit={limit}&offset={offset}"

    response = requests.request("GET", url, headers=headers, data=payload, files=files)

    games = response.json()

    if not games:
        stop = 1
    full_games = full_games + games
    offset = offset + 500

full_games_copy = copy.deepcopy(full_games)
filtered_games = []

for game in full_games:
    category = int(game.get("category"))
    if category == 0:
        platforms = game.get("platforms")
        check = any(item in platforms for item in consoles_ids)
        if check:
            filtered_games.append(game)

for game in filtered_games:
    first_release_date = game.get('first_release_date')
    if first_release_date:
        t = abs(int(first_release_date))
        game['first_release_date'] = datetime.utcfromtimestamp(t).strftime('%Y-%m-%d')
