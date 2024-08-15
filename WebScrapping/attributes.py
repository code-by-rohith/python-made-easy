import requests
from bs4 import BeautifulSoup

url= 'https://webscraper.io/test-sites'
value=requests.get(url)

soup = BeautifulSoup(value.text,'html.parser')
format= soup.find('div')
format1=format.attrs
print(format1)