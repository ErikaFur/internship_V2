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

@pytest.fixture(scope='class')
def response_champion_by_summonerName(open_options):
    data = open_options
    summonerName = data['summonerName']
    token = data["X-Riot-Token"]

    url = f"https://ru.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}"
    headers = {
        'X-Riot-Token': token
    }
    response = requests.request("GET", url, headers=headers)
    return response

@pytest.fixture(scope='class')
def response_champions_by_summonerId(open_options):
    data = open_options
    encryptedSummonerId = data['id']
    token = data["X-Riot-Token"]

    url = f"https://ru.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}"
    headers = {
        'X-Riot-Token': token
    }
    response = requests.request("GET", url, headers=headers)
    return response

@pytest.fixture(scope='class')
def response_champion_by_summonerId(open_options):
    data = open_options
    encryptedSummonerId = data['id']
    championId = 78
    token = data["X-Riot-Token"]

    url = f"https://ru.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}/by-champion/{championId}"
    headers = {
        'X-Riot-Token': token
    }
    response = requests.request("GET", url, headers=headers)
    return response

@pytest.fixture(scope='class')
def response_champion_rotation(open_options):
    data = open_options
    token = data["X-Riot-Token"]

    url = f"https://ru.api.riotgames.com/lol/platform/v3/champion-rotations"
    headers = {
        'X-Riot-Token': token
    }
    response = requests.request("GET", url, headers=headers)
    return response

