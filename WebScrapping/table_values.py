import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://ticker.finology.in/'
connection= requests.get(url)
element = BeautifulSoup(connection.text,'html.parser')
soup = element.find('table',class_='table table-sm table-hover screenertable')
soup2=soup.find_all('th')
data=[i.text for i in soup2]
df=pd.DataFrame(columns=data)


rows = soup.find_all("tr")

for i in rows[1:]:
    val=i.find_all("td")
    rows=[tr1.text.strip() for tr1 in val]
    l=len(df)
    df.loc[l]=rows

df['Day HighRs.'] =pd.to_numeric(df['Day HighRs.'],errors='coerce')
s=df['Day HighRs.'].sum()
print(df)
print(s)

