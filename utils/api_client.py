import requests
import os
from utils.logger import get_logger
from dotenv import load_dotenv

load_dotenv()
logger = get_logger()


class APIClient:

    BASE_URL = "https://reqres.in"

    @staticmethod
    def get_headers():

        api_key = os.getenv("API_KEY")

        headers = {
            "Content-Type": "application/json"
        }

        if api_key:
            headers["x-api-key"] = api_key

        return headers

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
            headers=APIClient.get_headers()
        )

        logger.info(f"Status Code: {response.status_code}")

        return response