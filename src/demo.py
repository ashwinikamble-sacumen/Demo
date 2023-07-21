"""This file for request module"""
from requests import Response
import requests


def fetch(url: str) -> Response:
    """Pass url to fetch method.

    Args:
        url (str): a string.

    Returns:
        Response: fetching the data from given url.
    """

    url = "https://catfact.ninja/fact"
    response = requests.get(url, timeout=2)
    print(f"Contents are : {response.content}")
    if response.status_code == 200:
        res = response.json()
        print(res)
    return "worng url passing"


fetch("https://catfact.ninja/fact")
