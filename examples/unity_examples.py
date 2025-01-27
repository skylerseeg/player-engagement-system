import requests

url = "http://localhost:8000/recommend"
player_id = 12345
response = requests.get(url, params={"player_id": player_id})
print("Recommendations:", response.json())
