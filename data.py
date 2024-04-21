import json
import csv
from datetime import datetime, timedelta

# Wczytaj dane z pliku JSON
with open("price_history.json", "r") as file:
    data = json.load(file)

# Funkcja do konwersji formatu daty
def convert_date(date_string):
    return datetime.strptime(date_string, "%b %d %Y %H: +0").strftime("%Y-%m-%d")

# Przefiltruj dane, usuwając ostatni miesiąc i duplikaty
filtered_data = []
seen_dates = set()

for item in data["prices"]:
    date = convert_date(item[0])
    if date not in seen_dates:
        seen_dates.add(date)
        filtered_data.append([date, item[1]])

# Posortuj dane według daty
filtered_data.sort(key=lambda x: x[0])

# Usuń dane z ostatniego miesiąca
month_ago = datetime.now() - timedelta(days=30)
filtered_data = [item for item in filtered_data if datetime.strptime(item[0], "%Y-%m-%d") < month_ago]

# Zapisz przefiltrowane dane do pliku CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Price"])
    writer.writerows(filtered_data)

print("Przefiltrowane dane zostały zapisane do pliku data.csv")

# Zapisz wszystkie dane do pliku CSV
all_data = []
seen_dates = set()

for item in data["prices"]:
    date = convert_date(item[0])
    if date not in seen_dates:
        seen_dates.add(date)
        all_data.append([date, item[1]])

all_data.sort(key=lambda x: x[0])

with open("data_all.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Price"])
    writer.writerows(all_data)

print("Wszystkie dane zostały zapisane do pliku data_all.csv")