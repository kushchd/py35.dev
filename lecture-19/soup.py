import sys

from bs4 import BeautifulSoup
import requests

url = 'https://news.ycombinator.com/'

content = requests.get(url).content

soup = BeautifulSoup(content, 'html.parser')

for item in soup.find_all('a', class_='storylink'):
    print(item.get_text())

sys.exit()
