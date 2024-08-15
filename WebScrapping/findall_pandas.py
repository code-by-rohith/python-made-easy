import re

import requests
from  bs4 import BeautifulSoup
import pandas as pd

url='https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
conn = requests.get(url)
soup = BeautifulSoup(conn.text,"lxml")
soup1 = soup.find_all('a',class_='title')
soup2 = soup.find_all('h4',class_='price float-end card-title pull-right')
data =[]
data2=[]
for i  in soup1:
    elem = i.text

    data.append(elem)

for j in soup2:
    elem =j.text
    data2.append(elem)



datas = pd.DataFrame({"Product Name":data,"Product Price":data2})
print(datas)