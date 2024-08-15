import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.meesho.com/cricket-bats/pl/9d7?srsltid=AfmBOor0OhKwgC3EwgK4td1Q3ISxXIaliQSbiCOPKyl2yswS5Z8Pg5l-"
connection = requests.get(url)
element = BeautifulSoup(connection.text, 'html.parser')

soup = element.find_all("p", class_='sc-eDvSVe gQDOBc NewProductCardstyled__StyledDesktopProductTitle-sc-6y2tys-5 ejhQZU NewProductCardstyled__StyledDesktopProductTitle-sc-6y2tys-5 ejhQZU')
soup2 = element.find_all("h5", class_='sc-eDvSVe dwCrSh')
soup3=element.findAll('span',class_='sc-eDvSVe laVOtN')


data = [i.text for i in soup]
data2 = [j.text for j in soup2]
data3=[z.text for z in soup3]

max_length = max(len(data), len(data2), len(data3))

data.extend([''] * (max_length - len(data)))
data2.extend([''] * (max_length - len(data2)))
data3.extend([''] * (max_length - len(data3)))

df = pd.DataFrame({"Bat Name": data, "Bat Price": data2,"Ratings":data3})


df['Bat Price'] = df['Bat Price'].str.replace('₹', '')  # Remove '₹'
df['Bat Price'] = df['Bat Price'].str.replace(' onwards', '')  # Remove 'onwards'
df['Bat Price'] = df['Bat Price'].str.replace(',', '')  # Remove commas

df['Bat Price'] = pd.to_numeric(df['Bat Price'], errors='coerce')
df['Ratings'] = pd.to_numeric(df['Ratings'], errors='coerce')


print(df)


total_sum = df['Bat Price'].sum()

print(f"Total Sum of Bat Prices: ₹{total_sum:.2f}")

df.to_csv("data.csv")

