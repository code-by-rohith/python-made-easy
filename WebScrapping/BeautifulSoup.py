import requests
from bs4 import BeautifulSoup

url= 'https://webscraper.io/test-sites'
value=requests.get(url)

soup = BeautifulSoup(value.text,'html.parser')
finding=soup.find('div')
formated_html=finding.prettify()

print(formated_html)
