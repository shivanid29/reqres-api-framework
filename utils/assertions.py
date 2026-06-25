def validate_status_code(response, expected_status):

    assert response.status_code == expected_status, \
        f"Expected {expected_status}, got {response.status_code}"


def validate_json_value(response, path, expected):

    data = response.json()

    keys = path.split(".")

    value = data

    for key in keys:
        value = value[key]

    assert value == expected, \
        f"Expected {expected}, got {value}"