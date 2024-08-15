import re

import requests
from  bs4 import BeautifulSoup

url='https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
conn = requests.get(url)
soup = BeautifulSoup(conn.text,"lxml")
# element = soup.find_all(string = ["Galaxy Tab 3"])
element = soup.find_all(string =re.compile( "Acer"))
print(element)