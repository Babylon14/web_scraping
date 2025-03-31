import requests
import bs4
from fake_headers import Headers


KEYWORDS = ['дизайн', 'фото', 'web', 'python']

responce = requests.get(url="https://habr.com/ru/companies/selectel/articles/",
                        headers=Headers(browser="chrome", os="mac").generate())

soup = bs4.BeautifulSoup(responce.text, features="lxml")
article_list = soup.find_all("article")


for article in article_list:
    '''Находим список заголовков'''
    pass