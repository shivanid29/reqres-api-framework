import json
import os
from dotenv import load_dotenv


def load_test_data():

    # Load .env only for local machine
    load_dotenv()

    with open("tests/test_data.json") as file:
        data = json.load(file)

    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    for test in data["test_cases"]:

        if "payload" in test:

            if "email" in test["payload"] and test["payload"]["email"] == "${EMAIL}":
                test["payload"]["email"] = email

            if "password" in test["payload"] and test["payload"]["password"] == "${PASSWORD}":
                test["payload"]["password"] = password

    return data