import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.geeksforgeeks.org/python-web-scraping-tutorial/')
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find('body')
content = s.find_all('p')
print(content)




