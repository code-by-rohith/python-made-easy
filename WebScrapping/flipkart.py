import pandas as pd
import requests
from bs4 import BeautifulSoup

name=[]
price=[]
review=[]
for i in range(1,31):
        url ='https://www.flipkart.com//audio-video/headset/pr?sid=0pm%2Cfcn&p%5B%5D=facets.connectivity%255B%255D%3DBluetooth&sort=popularity&p%5B%5D=facets.rating%255B%255D%3D3%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.price_range.from%3D599&p%5B%5D=facets.price_range.to%3DMax&p%5B%5D=facets.headphone_type%255B%255D%3DTrue%2BWireless&param=866&hpid=WqCPtE2MbDEYEbYbttXC1qp7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJHcmFiIE5vdyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6IkFDQ0ZTREdYWDNTNkRWQkciLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJCZXN0IFRydWV3aXJlbGVzcyBIZWFkcGhvbmVzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&page='+str(i)
        header ={
            "Accept":"* / *"
        }

        conn = requests.get(url,headers=header)
        soup = BeautifulSoup(conn.text,'html.parser')
        element= soup.find('div',class_='DOjaWF gdgoEp')
        element2= element.findAll('a',class_='wjcEIp')
        element3=element.find_all('div',class_='Nx9bqj')
        element4=element.find_all('span',class_='Y1HWO0')

        for i in element2:
            name.append(i.text)
        for j in element3:
            price.append(j.text)
        for k in element4:
            review.append(k.text)


df=pd.DataFrame({"Product Name ":name ,"Product Price":price ,"Review":review})
df['Product Price']=df['Product Price'].str.replace('₹','')
print(df.tail())
print(df.to_csv('final.csv'))
print(df)

