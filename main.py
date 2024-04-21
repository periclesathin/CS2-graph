import requests
import json

headers = {
    "Cookie": "ActListPageSize=10; bCompletedTradeOfferTutorial=true; cookieSettings=%7B%22version%22%3A1%2C%22preference_state%22%3A1%2C%22content_customization%22%3Anull%2C%22valve_analytics%22%3Anull%2C%22third_party_analytics%22%3Anull%2C%22third_party_content%22%3Anull%2C%22utm_enabled%22%3Atrue%7D; enableSIH=true; recentlyVisitedAppHubs=440%2C730; rgDiscussionPrefs=%7B%22cTopicRepliesPerPage%22%3A30%7D; sessionid=71a8fc115ba05611f534d85d; steamCountry=PL%7Cdd9e2137c9de6d028f4f0cbb70132345; steamLoginSecure=76561199496102974%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MUEwRF8yNDFCREEwOF9DQjhDQiIsICJzdWIiOiAiNzY1NjExOTk0OTYxMDI5NzQiLCAiYXVkIjogWyAid2ViOmNvbW11bml0eSIgXSwgImV4cCI6IDE3MTM3MzQxNTIsICJuYmYiOiAxNzA1MDA3MTgwLCAiaWF0IjogMTcxMzY0NzE4MCwgImp0aSI6ICIwRjA2XzI0NDg5RjM1XzI5NURGIiwgIm9hdCI6IDE3MTA2OTc0MjYsICJydF9leHAiOiAxNzI4ODU3NjcwLCAicGVyIjogMCwgImlwX3N1YmplY3QiOiAiMTQ5LjE1Ni4xMjQuMSIsICJpcF9jb25maXJtZXIiOiAiNS4xNzMuNDIuMjMiIH0.Z1KQZTdkb1VDqLBzJVwU537jBVVFhx7ypg5A7ivGseEk0CednHnvagcwjKMvQcsdd9mCfDlGXhXycyqt0gBGAQ; strInventoryLastContext=730_2; timezoneOffset=7200,0"
}

url = "https://steamcommunity.com/market/pricehistory/?country=PT&currency=3&appid=730&market_hash_name=Fracture%20Case"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    filename = "price_history.json"
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Dane zostały zapisane do pliku: {filename}")
else:
    print(f"Błąd pobierania danych. Kod statusu: {response.status_code}")