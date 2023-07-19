"""Get response."""

url = "https://api.publicapis.org/entries?limit=10"
offset = 0
limit = 10

while True:
    url = f"https://api.publicapis.org/entries?offset={offset}&limit={limit}"
    print("Response", url)
    offset = offset + 10
    if offset > 150:
        break
