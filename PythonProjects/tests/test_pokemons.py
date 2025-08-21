import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '10317eb8e4a015eeb0be2dd55a241216'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '42397'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_name():
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response.json()["data"][0]["trainer_name"] == 'Sasha'