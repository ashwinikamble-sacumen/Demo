"""Fetch python file."""

import logging
import requests
from requests import Response

logging.basicConfig(
    filename="fetched.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def fetch(url: str) -> Response:
    """Pass Url to the fetch method.

    Args:
        url (str): a string.

    Returns:
        str:Fetching data from given API.
    """
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        logging.info("Api call successful for %s", url)
        return data
    return logging.debug("wrong url")


fetch("https://catfact.ninja/fact")
