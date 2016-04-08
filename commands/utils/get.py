import requests


def health_check(url):
    return requests.get(url).status_code
