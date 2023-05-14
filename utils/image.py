import os
import requests

from config import config


def load(url):
    filename = 'image/' + url.split("/")[-1]
    if not os.path.exists(filename):
        response = requests.get(url)
        with open(filename, "wb") as f:
            f.write(response.content)
    return f'/{filename}'
