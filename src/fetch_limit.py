"""This file for request module"""
import requests


def fetch_item(limit):
    """Fecthing data from given url."""

    url = "https://slack.com/api/users.lisst"
    # url = "https://slack.com/api/conversations.list"

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer xoxp-4337539725382-4344140997698-4368338310656-594000c8fe5e632e45d51336a52a402b",  # noqa:E501
    }

    limit = 1
    slack_data = []
    for page_num in range(7):
        offset = page_num + limit
        url = f"https://slack.com/api/users.list?offset={offset}&limit={limit}"
        print(f"response {url}")

        response = requests.get(url, headers=headers, timeout=2)
        res = response.json()
        print("-----------")
        print(res["members"])
        slack_data.extend(res["members"])
        # print(slack_data[0])


fetch_item("https://slack.com/api/users.list")
