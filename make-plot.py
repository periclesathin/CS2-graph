import csv
from datetime import datetime
import plotly.graph_objs as go

def plot_data(market_hash_names, num_days):
    fig = go.Figure()

    for name in market_hash_names:
        # Wczytaj dane z pliku CSV
        filename = f"{name.replace('%20', '_')}.csv"
        dates = []
        prices = []

        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Pomiń nagłówek
            for row in reader:
                dates.append(datetime.strptime(row[0], "%Y-%m-%d"))
                prices.append(float(row[1]))

        # Oblicz liczbę dni od początku
        start_date = min(dates)
        days = [(date - start_date).days for date in dates]

        # Ogranicz dane do określonej liczby pierwszych dni
        days = days[:num_days]
        prices = prices[:num_days]

        # Dodaj dane do wykresu
        trace = go.Scatter(x=days, y=prices, mode='lines+markers', name=name)
        fig.add_trace(trace)

    fig.update_layout(
        title="SCM Price PLN",
        xaxis_title="Days after release",
        yaxis_title="Price",
        hovermode="closest"
    )

    # Stwórz nazwę pliku na podstawie nazw z legendy
    legend_names = [name.replace("%20", "_") for name in market_hash_names]
    filename = "-".join(legend_names) + "_interactive_plot.html"

    # Zapisz wykres interaktywny jako plik HTML
    fig.write_html(filename)

# Przykładowe użycie
market_hash_names = ["Fracture_Case", "Prisma_Case", "Shattered_Web_Case"]
num_days = 30

plot_data(market_hash_names, num_days)