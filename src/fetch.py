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
    payload = {}
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer xoxp-4337539725382-4344140997698-4368338310656-594000c8fe5e632e45d51336a52a402b",  # noqa: E501
    }

    response = requests.get(url, headers=headers, data=payload, timeout=10)

    if response.status_code == 200:
        res = response.json()
        print(res["members"])
    return "worng url passing"


fetch("https://slack.com/api/users.list")
