import json


def load_test_data():

    with open("tests/test_data.json") as file:

        return json.load(file)