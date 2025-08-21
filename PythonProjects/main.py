import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '10317eb8e4a015eeb0be2dd55a241216'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_creation = {
    "name": "python",
    "photo_id": 69
}

body_change = {
    "pokemon_id": "378340",
    "name": "New Name",
    "photo_id": 69
}

body_get_pokemon = {
    "pokemon_id": "378340"
}

response_creation = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creation)
print(response_creation.text)

pokemon_id = response_creation.json()['id']
print(pokemon_id)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_get_pokemon = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_get_pokemon)
print(response_get_pokemon.text)