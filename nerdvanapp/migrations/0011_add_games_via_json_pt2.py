import json
from django.db import migrations, models
import requests
from iso3166 import countries


def create_games(apps, schema_editor):
    # 1) Import Models
    game_company_model = apps.get_model("nerdvanapp", "GameCompany")
    game_model = apps.get_model("nerdvanapp", "Games")
    console_model = apps.get_model("nerdvanapp", "Console")

    # 2) Request Headers
    headers = {
        'Client-ID': '3d2zdvuspo8925eerye9r9etrs67dd',
        'Authorization': 'Bearer v4r49hyi6hf9u8147hza6t3tg04qmi',
        'Accept': 'application/json'
    }

    # 3) Read games from Json
    games_data = open(r"\Users\Marcos Oliveira\PycharmProjects\NerdvanaAPI\nerdvanapp\scripts\games_v3.json")
    games = json.load(games_data)
    games = games[4000:8000]

    # 4) Create GameCompany and Game
    filtered_games = games
    g = 0
    for game in filtered_games:
        print(f"[ID:{g}] Adding {game.get('name')} to the database")
        g = g + 1
        related_game_company = None
        involved_companies = game.get('involved_companies')
        if involved_companies:
            involved_companies_id = involved_companies[0]
            url = f"https://api.igdb.com/v4/involved_companies/{involved_companies_id}?fields=company"
            response = requests.request("GET", url, headers=headers)
            company = response.json()
            if company:
                company_id = company[0].get('company')
                url = f"https://api.igdb.com/v4/companies/{company_id}?fields=name,%20description,%20country"
                response = requests.request("GET", url, headers=headers)
                game_company = response.json()
                if game_company:
                    game_company_element = game_company[0]
                    game_company_name = game_company_element.get('name')
                    company_exists = game_company_model.objects.filter(name=game_company_name).exists()
                    if not company_exists:
                        country = game_company_element.get('country')
                        if country:
                            game_company_element['country'] = countries.get(country).name
                        related_game_company = game_company_model(
                            name=game_company_element.get('name'),
                            country=game_company_element.get('country'),
                            description=game_company_element.get('description')
                        )
                        related_game_company.save()
                    else:
                        related_game_company = game_company_model.objects.filter(name=game_company_name).first()
        # 4.1) Get related consoles
        related_consoles_ids = game.get('platforms')
        related_consoles = console_model.objects.filter(twitch_id__in=related_consoles_ids)

        # 4.2) Save game model
        new_game_name = game.get('name')
        game_exists = game_model.objects.filter(name=new_game_name).exists()
        if not game_exists:
            new_game = game_model.objects.create(
                name=game.get('name'),
                release=game.get('first_release_date'),
                summary=game.get('summary'),
                storyline=game.get('storyline'),
                game_company=related_game_company,
                rating=game.get('rating'),
                rating_count=game.get('rating_count'),
            )

            for console in related_consoles:
                new_game.console.add(console)

            new_game.save()


class Migration(migrations.Migration):

    dependencies = [
        ('nerdvanapp', '0010_alter_games_name'),
    ]

    operations = [
        migrations.RunPython(create_games),
    ]
