import requests
import os
from utils.logger import get_logger
from dotenv import load_dotenv


logger = get_logger()

load_dotenv()  # loads .env locally

class APIClient:

    BASE_URL = "https://reqres.in"

    API_KEY = os.getenv("API_KEY")

    HEADERS = {
        "x-api-key": API_KEY
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