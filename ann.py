import requests
from bs4 import BeautifulSoup
import pandas as pd
import config

def contains_substring(str, substrs):
    for substring in substrs:
        if substring in str:
            return True
    return False
    
def get_ann():
    """
    Get the ANN list from bitcointalk.org
    """
    print("Getting ANN list...")
    url = 'https://bitcointalk.org/index.php?board=159.0'  # ANN URL

    response = requests.get(url)
    if response.status_code == 200:
        # use BeautifulSoup to parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = pd.read_html(str(soup))
        df = tables[7] # ANN list table
        dict_array = df.to_dict(orient='records')
        dict_array = dict_array[1:]
        for i in range(len(dict_array)):
            item = dict_array[i]
            subject = item[2]
            author = item[3]
            comment = int(item[4])
            read = int(item[5])
            last_time = item[6]
            lower_subject = subject.lower()
            if comment <= config.comment_ceil and read <= config.read_ceil and contains_substring(lower_subject, config.keywords):
                print(f"found! {subject} {author} {comment} {read} {last_time}")
    else:
        print(f"request failed, the status code is: {response.status_code}")

get_ann()
