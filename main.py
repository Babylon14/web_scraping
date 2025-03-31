import requests
import bs4
from fake_headers import Headers


responce = requests.get(url="https://habr.com/ru/companies/selectel/articles/",
                        headers=Headers(browser="chrome", os="mac").generate())
print(responce.request.headers)