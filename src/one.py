"""Get response."""

import json
import requests

# url = "https://api.publicapis.org/entries?limit=10"
# offset = 0
# limit = 10

# while True:
#     url = f"https://api.publicapis.org/entries?offset={offset}&limit={limit}"
#     print("Response", url)
#     offset = offset + 10
#     if offset > 150:
#         break

url = "https://api.publicapis.org/entries?limit=10"
entry = []
offset = 0
limit = 10

for pg in range(10):
    offset = pg * limit
    url = f"https://api.publicapis.org/entries?offset={offset}&limit={limit}"
    print(url)
    response = requests.get(url, timeout=2)
    data = response.json()
    try:
        print(data["entries"])
    except json.decoder.JSONDecodeError:
        entry.extend(data["entries"])
