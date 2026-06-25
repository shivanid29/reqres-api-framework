import pytest

from utils.api_client import APIClient
from utils.assertions import (
    validate_status_code,
    validate_json_value
)
from utils.json_reader import load_test_data


test_cases = load_test_data()["test_cases"]


@pytest.mark.parametrize("test_data", test_cases)
def test_reqres_api(test_data):

    response = APIClient.send_request(
        method=test_data["method"],
        endpoint=test_data["endpoint"],
        payload=test_data.get("payload")
    )

    validate_status_code(
        response,
        test_data["expected_status"]
    )

    assertions = test_data.get("assertions", [])

    for assertion in assertions:

        validate_json_value(
            response,
            assertion["path"],
            assertion["expected"]
        )