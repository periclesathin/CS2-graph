CS2 Graph Price Comparasion         
    This project is designed to track and analyze the prices of cases in the Counter-Strike: Global Offensive (CS:GO) game on the Steam Community Market.

Features
1. Scraper (scraper.py)
This script fetches historical price data for selected cases from the Steam Community Market.
import requests
import json

```env
def scrape_data(market_hash_name):
    # Scraper code
    ...
```

Example Usage
```env
market_hash_names = ["Fracture%20Case", "Prisma%20Case", "Shattered%20Web%20Case"]
for name in market_hash_names:
    scrape_data(name)
```

2. Data Processing (data.py)
This script processes the fetched data, removes duplicates, and saves it in CSV format.
```env
import json
import csv
from datetime import datetime
def process_data(market_hash_name):
    # Data processing code
    ...
```

Example Usage
```env
market_hash_names = ["Fracture%20Case", "Prisma%20Case", "Shattered%20Web%20Case"]
for name in market_hash_names:
    process_data(name)
```

3. Data Visualization (make-plot.py)
```env
import csv
from datetime import datetime
import plotly.graph_objs as go
def plot_data(market_hash_names, num_days):
    # Data visualization code
    ...
```

Example Usage
```env
market_hash_names = ["Fracture_Case", "Prisma_Case", "Shattered_Web_Case"]
num_days = 30
plot_data(market_hash_names, num_days)
```

4. Local Server (server.py)
This script runs a local HTTP server, which allows you to view the generated HTML files with charts.
```env
import http.server
import socketserver
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
```
Screenshots:    
Example Interactive Chart
![image](https://github.com/periclesathin/CS2-graph/assets/166219501/78abb8d8-610e-45c6-941b-817ca8c79233)    
Example CSV Data    
![image](https://github.com/periclesathin/CS2-graph/assets/166219501/bbbf9f01-5052-48ea-9141-7f6fb8a678f9)    
Usage Instructions    
Install the required Python libraries (requests, plotly).    
Run the main.py script to fetch historical price data for the selected cases.    
Run the data.py script to process the fetched data and save it in CSV format.    
Run the plot.py script to generate an interactive line chart displaying the price history.    
Run the server.py script to start a local HTTP server and view the generated HTML files with charts.    


