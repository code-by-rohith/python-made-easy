import requests
from bs4 import BeautifulSoup

url =  'https://webscraper.io/test-sites/e-commerce/allinone/product/3'
html_get=requests.get(url)
soup=BeautifulSoup(html_get.text,'html.parser')
element=(soup.find('h4',{"class":"price float-end pull-right"}))
print(element.string)
