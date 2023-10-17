import random

import requests


def random_number(x, y):
    return random.randint(x, y)


def random_word(arr=None):
    if arr is None:
        arr = []
    return random.choice(arr)

# Not yet really correct
def random_joke(category=None):

    if category is None:
        api_url = "https://witzapi.de/api/joke"
    if category is not None:
        api_url = "https://witzapi.de/api/joke?" + category
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        text_value = data[0]["text"]
        return text_value
    return "Sorry, Joke fabric down"



print(random_joke())
