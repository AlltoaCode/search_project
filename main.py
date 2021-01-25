import requests
from bs4 import BeautifulSoup

r = requests.get('https://en.wikipedia.org/wiki/Main_Page')
print(r.status_code)
print(r.json())