import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.python.org')
print(int(r.status_code))

soup = BeautifulSoup(r.text, 'html.parser')
soup = soup.prettify()
print(soup)

soup.