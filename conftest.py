import json
import pytest
import requests


@pytest.fixture(scope='session')
def open_options():
    with open("options.json", "r") as read_file:
        data = json.load(read_file)
        return data

@pytest.fixture(scope='class')
def response_account_by_puuid(open_options):
    data = open_options
    puuid = data['puuid']
    token = data["X-Riot-Token"]

    url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}"
    headers = {
        'X-Riot-Token': token
    }
    response = requests.request("GET", url, headers=headers)
    return response

@pytest.fixture(scope='class')
def response_account_by_gameName(open_options):
    data = open_options
    gameName = data['name']
    tagLine = data['tagLine']
    token = data["X-Riot-Token"]

    url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}"
    headers = {
        'X-Riot-Token': token
    }
    response = requests.request("GET", url, headers=headers)
    return response

@pytest.fixture(scope='class')
def response_account_area(open_options):
    data = open_options
    puuid = data['puuid']
    token = data["X-Riot-Token"]

    url = f"https://europe.api.riotgames.com/riot/account/v1/active-shards/by-game/val/by-puuid/{puuid}"
    headers = {
        'X-Riot-Token': token
    }
    response = requests.request("GET", url, headers=headers)
    return response