import requests
from bs4 import BeautifulSoup

url =  'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
html_get=requests.get(url)
soup=BeautifulSoup(html_get.text,'lxml')
element=(soup.findAll('h4',class_='price float-end card-title pull-right'))
element1=soup.find('p',class_='description card-text')
element2=soup.find('a',class_= 'title')
print("Product Name - ",element2.text)
for i in element[0]:
    print("Product Price - ",i.text)
print("Product Discription - ",element1.text)