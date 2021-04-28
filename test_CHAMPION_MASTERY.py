import json
import pytest
import requests
import functions

class TestInfoBySummonerName():
    def test_info_by_SummonerName(self, response_champion_by_summonerName):
        response = response_champion_by_summonerName
        functions.is_response_JSON_format(response)
        functions.is_response_status_200(response)

    def test_info_by_SummonerName_contains_puuid(self, response_champion_by_summonerName):
        response = response_champion_by_summonerName
        response_json = json.loads(response.text)
        functions.is_presented_in_JSON(response_json, "puuid")

    def test_info_by_SummonerName_contains_id(self, response_champion_by_summonerName):
        response = response_champion_by_summonerName
        response_json = json.loads(response.text)
        functions.is_presented_in_JSON(response_json, "id")

    def test_info_by_SummonerName_contains_accountId(self, response_champion_by_summonerName):
        response = response_champion_by_summonerName
        response_json = json.loads(response.text)
        functions.is_presented_in_JSON(response_json, "accountId")

    def test_info_by_SummonerName_contains_lvl(self, response_champion_by_summonerName):
        response = response_champion_by_summonerName
        response_json = json.loads(response.text)
        functions.is_presented_in_JSON(response_json, "summonerLevel")

    def test_info_by_SummonerName_correct_lvl(self, response_champion_by_summonerName):
        response = response_champion_by_summonerName
        response_json = json.loads(response.text)
        functions.is_JSON_tag_contains_type(response_json, "summonerLevel", int)
        assert response_json["summonerLevel"] > 0

class TestChampionsInfoBySummonerId():
    def test_responce_info_by_SummonerId(self, response_champions_by_summonerId):
        response = response_champions_by_summonerId
        functions.is_response_JSON_format(response)
        functions.is_response_status_200(response)

    def test_list_sorted_by_championLevel(self, response_champions_by_summonerId):
        response = response_champions_by_summonerId
        response_json = json.loads(response.text)
        functions.is_sorted_by_tag_from_biggest_to_smallest(response_json, "championLevel")

    @pytest.mark.xfail(reason="list does not supposed to be ordered by championID")
    def test_list_sorted_by_championLevel(self, response_champions_by_summonerId):
        response = response_champions_by_summonerId
        response_json = json.loads(response.text)
        functions.is_sorted_by_tag_from_biggest_to_smallest(response_json, "championId")

class TestChampionInfoBySummonerIdAndChampionId():
    def test_responce_info_by_SummonerId_and_ChampionId(self, response_champion_by_summonerId):
        response = response_champion_by_summonerId
        functions.is_response_JSON_format(response)
        functions.is_response_status_200(response)

    def test_list_sorted_by_championLevel(self, response_champion_by_summonerId):
        response = response_champion_by_summonerId
        response_json = json.loads(response.text)
        functions.is_presented_in_JSON(response_json, "championLevel")
