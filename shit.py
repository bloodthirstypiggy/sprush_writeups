import requests
from bs4 import BeautifulSoup

url='http://study.sprush.rocks:15428/'
ssilka='q99De891XA'

while True:
    responce = requests.get(url+ssilka)
    soup = BeautifulSoup(responce.text, 'lxml')
    quotes = soup.find_all('div', class_ = 'real_link')
    print(quotes[0].text)
    print(url+quotes[0].text.replace('\n', ''))
    ssilka = quotes[0].text.replace('\n', '')
