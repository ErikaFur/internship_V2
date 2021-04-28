

def is_response_status_200(response):
    assert response.status_code == 200, f"status code should be 200, got {response.status_code}"

def is_presented_in_JSON(response_json, tag):
    assert tag in response_json, f"response does not contain tag {tag}"