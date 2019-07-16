from bs4 import BeautifulSoup
import requests

URL = "https://www.pepper.pl/promocje/zotac-geforce-rtx-2060-amp-6gb-gddr6-amazonde-170774"
URL_MAIN = "https://www.pepper.pl/grupa/audiowizualne-nowe"

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0"}

page = requests.get(URL, headers=headers)
page_second = requests.get(URL_MAIN, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
soup_second = BeautifulSoup(page_second.content, 'html.parser')

title = soup.find(attrs={"class": "thread-title"}).get_text().strip()
price = soup.find(attrs={"class": "thread-price"}).get_text()

articles = soup_second.find_all(attrs={'class': 'thread--deal'})
for article in articles:
    print(article.find(attrs={'class': 'thread-title'}).get_text())
    print(article.find(attrs={"class": "thread-price"}).get_text())