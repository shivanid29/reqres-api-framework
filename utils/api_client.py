import requests

from utils.logger import get_logger


logger = get_logger()


class APIClient:

    BASE_URL = "https://reqres.in"

    HEADERS = {
        "x-api-key": "pub_f9c9fbd8014447c836a03c42a7e91fbbfe00199826b02be15107cf4b865604fc"
    }

    @staticmethod
    def send_request(method, endpoint, payload=None):

        url = f"{APIClient.BASE_URL}{endpoint}"

        logger.info(f"{method} {url}")

        if payload:
            logger.info(f"Payload: {payload}")

        response = requests.request(
            method=method,
            url=url,
            json=payload,
            headers=APIClient.HEADERS
        )

        logger.info(f"Status Code: {response.status_code}")

        return response