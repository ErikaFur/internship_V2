import json
import pytest
import functions

class TestInfoChampion():
    def test_info_Champions_rotations(self, response_champion_rotation):
        response = response_champion_rotation
        functions.is_response_JSON_format(response)
        functions.is_response_status_200(response)

    def test_info_by_Champions_rotations_contains_freeChampionIds(self, response_champion_rotation):
        response = response_champion_rotation
        response_json = json.loads(response.text)
        functions.is_presented_in_JSON(response_json, "freeChampionIds")

    def test_info_by_Champions_rotations_contains_freeChampionIdsForNewPlayers(self, response_champion_rotation):
        response = response_champion_rotation
        response_json = json.loads(response.text)
        functions.is_presented_in_JSON(response_json, "freeChampionIdsForNewPlayers")

    def test_info_by_Champions_rotations_contains_maxNewPlayerLevel(self, response_champion_rotation):
        response = response_champion_rotation
        response_json = json.loads(response.text)
        functions.is_presented_in_JSON(response_json, "maxNewPlayerLevel")