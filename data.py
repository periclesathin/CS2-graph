import json
import csv
from datetime import datetime

def process_data(market_hash_name):
    # Wczytaj dane z pliku JSON
    with open(f"{market_hash_name.replace('%20', '_')}.json", "r") as file:
        data = json.load(file)

    # Funkcja do konwersji formatu daty
    def convert_date(date_string):
        return datetime.strptime(date_string, "%b %d %Y %H: +0").strftime("%Y-%m-%d")

    # Przetwórz dane, usuwając duplikaty
    processed_data = []
    seen_dates = set()

    for item in data["prices"]:
        date = convert_date(item[0])
        if date not in seen_dates:
            seen_dates.add(date)
            processed_data.append([date, item[1]])

    # Posortuj dane według daty
    processed_data.sort(key=lambda x: x[0])

    # Zapisz przetworzone dane do pliku CSV
    filename = f"{market_hash_name.replace('%20', '_')}.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Price"])
        writer.writerows(processed_data)

    print(f"Przetworzone dane dla {market_hash_name} zostały zapisane do pliku: {filename}")

# Przykładowe użycie
market_hash_names = ["Fracture%20Case", "Prisma%20Case", "Shattered%20Web%20Case"]

for name in market_hash_names:
    process_data(name)