import logging

import requests

api_url = "https://api.nekosapi.com/v3/"


def get_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()


def get_image(nsfw=False):
    data = get_api(api_url + "images/random?limit=5")
    for item in data['items']:
        is_fine = False
        for tags in item['tags']:
            if tags['is_nsfw']:
                is_fine = True
        if is_fine == nsfw:
            logging.info(item)
            return item['image_url']

