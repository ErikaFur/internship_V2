import json
import pytest
import requests
import functions

class TestAccountInfoUserName():
    def test_account_info_by_userName(self, response_account_by_gameName):
        response = response_account_by_gameName
        functions.is_response_status_200(response)

    def test_account_info_by_userName_contains_puuid(self, response_account_by_gameName):
        response = response_account_by_gameName
        response_json = json.loads(response.text)
        functions.is_presented_in_JSON(response_json, "puuid")

    def test_account_info_by_userName_contains_gameName(self, response_account_by_gameName):
        response = response_account_by_gameName
        response_json = json.loads(response.text)
        functions.is_presented_in_JSON(response_json, "gameName")

    def test_account_info_by_userName_contains_tagLine(self, response_account_by_gameName):
        response = response_account_by_gameName
        response_json = json.loads(response.text)
        functions.is_presented_in_JSON(response_json, "tagLine")
    @pytest.mark.xfail(reason="special case to demonstrate xfail")
    def test_xfail(self, response_account_by_gameName):
        response = response_account_by_gameName
        response_json = json.loads(response.text)
        assert len(response_json) != 3