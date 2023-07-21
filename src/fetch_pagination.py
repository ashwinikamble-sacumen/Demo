"""This file for pagination demo."""

import requests


def fetch_item(limit):
    """Fecthing data from given url."""

    url = "https://catfact.ninja/fact"
    # url = "https://slack.com/api/conversations.list"

    limit = 2
    data = []
    for page_num in range(7):
        offset = page_num * limit
        url = f"https://catfact.ninja/fact?offset={offset}&limit={limit}"
        print(f"response {url}")

        response = requests.get(url, timeout=2)
        res = response.json()
        print("-----------")
        print(res["fact"])
        data.extend(res["fact"])
        # print(slack_data[0])


fetch_item("https://slack.com/api/users.list")
