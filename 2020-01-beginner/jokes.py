import requests

r = requests.get("https://reddit.com/r/dadjokes.json")

data = r.json()
print(data)
