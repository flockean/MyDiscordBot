import os
import requests
import random
import logging
from pathlib import Path


# Project
def file_path(file):
    return os.path.join(get_project_root(), "ressource", file)


def get_project_root() -> Path:
    return Path(__file__).parent.parent


# Random Parts
def random_number(x, y):
    return random.randint(x, y)


def random_word(arr=None):
    if arr is None:
        arr = []
    return random.choice(arr)


# Not yet really correct
def random_joke():
    api_url = "https://witzapi.de/api/joke"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        text_value = data[0]["text"]
        logging.info("response: " + text_value)
        return text_value
    return "Sorry Witze gehen leider gerade nicht ;("