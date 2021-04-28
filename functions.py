def is_response_status_200(response):
    assert response.status_code == 200, f"status code should be 200, got {response.status_code}"


def is_presented_in_JSON(response_json, tag):
    assert tag in response_json, f"response does not contain tag {tag}"


def is_response_JSON_format(response):
    assert 'application/json' in response.headers.get(
        'content-type'), f"format should be application/json, but got {response.headers.get('content-type')}"


def is_JSON_tag_contains_type(response_json, tag, obj_type):
    assert type(response_json[
                    tag]) == obj_type, f"object type {type(response_json['summonerLevel'])} does not equal to object type {obj_type}"

def is_sorted_by_tag_from_biggest_to_smallest(response_json, tag):
    pivot = 1000000
    for i in response_json:
        assert pivot >= i[tag], "The list is not sorted!"
        if pivot > i[tag]:
            pivot = i[tag]