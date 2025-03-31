import requests
import bs4
from fake_headers import Headers


KEYWORDS = ['дизайн', 'фото', 'web', 'python']

responce = requests.get(url="https://habr.com/ru/companies/selectel/articles/",
                        headers=Headers(browser="chrome", os="mac").generate())

soup = bs4.BeautifulSoup(responce.text, features="lxml")
article_list = soup.find_all("article")


result_list = []

for article in article_list:
    '''Находим список заголовков'''
    title_tag = article.find("h2", class_="tm-title tm-title_h2")
    if not title_tag:
        continue

    title = title_tag.text.strip()
    if not any(key.lower() in title.lower() for key in KEYWORDS):
        continue
    

    '''Находим список ссылок на статьи'''
    link_tag = title_tag.find("a", class_="tm-title__link")
    if link_tag:
        link = "https://habr.com" + link_tag["href"]
    else:
        link = "Ссылка не найдена"
    
    
    '''Находим даты статей'''
    date_tag = article.find("time")
    if date_tag:
        date = date_tag["datetime"].split("T")[0]
    else:
        date = "Дата не найдена"
    
    result_list.append(f"{date} - {title} - {link}")
    