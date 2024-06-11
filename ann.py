import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://bitcointalk.org/index.php?board=159.0'  # ANN URL

response = requests.get(url)
if response.status_code == 200:
    # use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    tables = pd.read_html(str(soup))
    df = tables[7] # ANN list table
    print(df)
else:
    print(f"request failed, the status code is: {response.status_code}")
