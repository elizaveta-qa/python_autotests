import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'ec2799895d33c530a365c63d91c5566f'
HEADERS = {'Content-Type' : 'application/json',
           'trainer_token' : TOKEN}

body = {

    "name": "LALA",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_name = {
    "pokemon_id": "14587",
    "name": "LALE",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)

print (response.text)

response_name = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_name)

print (response_name.text)