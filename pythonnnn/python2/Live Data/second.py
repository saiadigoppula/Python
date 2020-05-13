from bs4 import BeautifulSoup
import requests
import time

Keyword = 'NSE: RELIANCE'
site = "https://finance.google.com/finance?q={}&output=json".format(Keyword)

for x in range(100):
    html = requests.get(site, headers={'user-Agent':'Mozilla/5.0'}).content
    soup = BeautifulSoup(html,'html.parser')
    div = soup.find('div',class_='BNeawe iBp4i AP7Wnd')
    time.sleep(1)
    print(div.text.split(' ')[0])

