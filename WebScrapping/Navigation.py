import requests
from bs4 import BeautifulSoup

url= 'https://webscraper.io/test-sites'
value=requests.get(url)

soup = BeautifulSoup(value.text,'html.parser')
finding=soup.header.a.span
print(finding.string)




