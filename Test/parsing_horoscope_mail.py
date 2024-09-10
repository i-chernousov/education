from bs4 import BeautifulSoup
import requests

url = "https://horo.mail.ru/prediction/aries/today/"

response = requests.get(url)
bs = BeautifulSoup(response.text,"lxml")

element = bs.find(class_="article__item article__item_alignment_left article__item_html")

print(element.text)
