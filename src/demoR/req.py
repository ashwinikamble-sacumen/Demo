"""This file for request module."""

import logging
import requests

logging.basicConfig(filename="req.log", level=logging.INFO, filemode="w")

payload = {"page": 1, "count": 2}
"""Get request"""
response = requests.get(
    url="https://postman-echo.com/get", timeout=2, params=payload
)  # noqa: E501
logging.info(response.url)
logging.info(response.json())


payload = {"username": "ashwini", "password": "sacumen"}
"""Post request."""
response1 = requests.post(
    url="https://postman-echo.com/post", timeout=2, data=payload
)  # noqa: E501

logging.info(response1.text)
r = response1.json()
logging.info(r["headers"])
