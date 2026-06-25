import os


def pytest_sessionstart():

    os.makedirs("reports", exist_ok=True)