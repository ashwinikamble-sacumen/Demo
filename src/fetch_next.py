"""Python file to test api."""
import requests
from requests import Response


def fetch_next(url) -> Response:
    """Fetch method to test api."""
    url = "https://api.publicapis.org/entries"
    response = requests.get(url, timeout=3)
    data = response.json()
    print(data["count"])


fetch_next("https://api.publicapis.org/entries")
