import requests
from bs4 import BeautifulSoup

r = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')
print(r)
soup = BeautifulSoup(r.content, 'html.parser')
class_list = set()
a_tag = soup.find('div')
href_value = a_tag['class']
tags = {tag.name for tag in soup.find_all()}
for tag in tags:
    for i in soup.find_all(tag):
        if i.has_attr("class"):
            if len(i['class']) != 0:
                class_list.add(" ".join(i['class']))


print(class_list)