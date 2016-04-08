import requests


def health_check(url):
    try:
        return requests.get(url).status_code
    except Exception:
        return 729
