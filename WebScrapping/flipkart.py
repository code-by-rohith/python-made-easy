import requests
from bs4 import BeautifulSoup
url="https://www.google.com"
conn=requests.get(url)
soup = BeautifulSoup(conn.text,'html.parser')
print(soup)