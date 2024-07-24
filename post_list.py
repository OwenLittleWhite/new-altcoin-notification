import requests
from bs4 import BeautifulSoup
import config
import my_email
import time
from datetime import datetime
def contains_substring(str, substrs):
    str = str.lower()
    for substring in substrs:
        if substring in str:
            return True
    return False
    
def get_ann(url, table_index, name):
    """
    Get the ANN list from bitcointalk.org
    """
    print(f"{datetime.now()}: Getting {name} list...")
    response = requests.get(url)
    if response.status_code == 200:
        # use BeautifulSoup to parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table')
        list = tables[table_index] # ANN list table
        rows = list.find_all('tr')
        rows = rows[1:]
        res_arr = []
        for row in rows:
            cols = row.find_all(['td', 'th'])
            data = {}
            title_link = cols[2].find_all('a')[0]
            data['link'] = title_link.get('href')
            data['title'] = title_link.text.replace('\n', '').replace('\t', '').replace('\r', '').strip()
            data['author'] = cols[3].text.replace('\n', '').replace('\t', '').replace('\r', '').strip()
            data['replies'] = int(cols[4].text.replace('\n', '').replace('\t', '').replace('\r', '').strip())
            data['views'] = int(cols[5].text.replace('\n', '').replace('\t', '').replace('\r', '').strip())
            data['last_post'] = cols[6].text.replace('\n', '').replace('\t', '').replace('\r', '').strip()
            res_arr.append(data)
            # contains_substring(data['title'], config.keywords) and
            if data['replies'] < config.reply_ceil and data['views'] < config.view_ceil:
                my_email.send_email(data)
                print(f"{datetime.now()}: ", data)
            
    else :
        print(f"request failed, the status code is: {response.status_code}")

boards = [{
    'url': 'https://bitcointalk.org/index.php?board=159.0',  # ANN URL
    'name': 'Announcements',
    'table_index': 8
},{
    'url': 'https://bitcointalk.org/index.php?board=240.0',  # ANN URL
    'name': 'Announcements Token',
    'table_index': 7
}]

for board in boards:
    get_ann(board['url'], board['table_index'], board['name'])
    time.sleep(10)
