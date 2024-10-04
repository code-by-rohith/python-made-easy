import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.express as px
import streamlit as st

# Scraping setup
name = []
price = []
review = []

for i in range(1, 31):
    url = 'https://www.flipkart.com//audio-video/headset/pr?sid=0pm%2Cfcn&p%5B%5D=facets.connectivity%255B%255D%3DBluetooth&sort=popularity&p%5B%5D=facets.rating%255B%255D%3D3%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.price_range.from%3D599&p%5B%5D=facets.price_range.to%3DMax&p%5B%5D=facets.headphone_type%255B%255D%3DTrue%2BWireless&param=866&hpid=WqCPtE2MbDEYEbYbttXC1qp7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJHcmFiIE5vdyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6IkFDQ0ZTREdYWDNTNkRWQkciLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJCZXN0IFRydWV3aXJlbGVzcyBIZWFkcGhvbmVzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&page='+str(i)
    header = {"Accept":"* / *"}
    conn = requests.get(url, headers=header)
    soup = BeautifulSoup(conn.text, 'html.parser')

    element = soup.find('div', class_='DOjaWF gdgoEp')
    element2 = element.findAll('a', class_='wjcEIp')
    element3 = element.find_all('div', class_='Nx9bqj')
    element4 = element.find_all('span', class_='Y1HWO0')

    for i in element2:
        name.append(i.text)
    for j in element3:
        price.append(j.text.replace('₹', '').replace(',', ''))  # Clean the price
    for k in element4:
        review.append(k.text)

# Check array lengths
print(f"Length of name: {len(name)}")
print(f"Length of price: {len(price)}")
print(f"Length of review: {len(review)}")

# Adjust the arrays to have the same length by trimming them to the minimum length
min_length = min(len(name), len(price), len(review))

name = name[:min_length]
price = price[:min_length]
review = review[:min_length]

# Create a DataFrame
df = pd.DataFrame({"Product Name": name, "Product Price": price, "Review": review})

# Convert columns to appropriate types
df['Product Price'] = pd.to_numeric(df['Product Price'], errors='coerce')  # Handle non-numeric data
df['Review'] = pd.to_numeric(df['Review'], errors='coerce')

# Save DataFrame to CSV
df.to_csv('final.csv', index=False)

# Streamlit App with Plotly Visualizations
st.title("Flipkart Bluetooth Headphones Data")
st.write(df)

# Bar plot of product prices
fig1 = px.bar(df, x='Product Name', y='Product Price', title='Product Price Comparison', labels={'Product Price': 'Price (₹)'})
st.plotly_chart(fig1)

# Histogram of reviews
fig2 = px.histogram(df, x='Review', nbins=20, title='Review Distribution')
st.plotly_chart(fig2)

# Scatter plot showing the relationship between price and reviews
fig3 = px.scatter(df, x='Product Price', y='Review', title='Price vs Reviews',
                  labels={'Product Price': 'Price (₹)', 'Review': 'Review Score'},
                  hover_name='Product Name', trendline="ols")
st.plotly_chart(fig3)

# Box plot to show the price range and identify outliers
fig4 = px.box(df, y='Product Price', title='Price Range and Outliers', points='all',
              labels={'Product Price': 'Price (₹)'})
st.plotly_chart(fig4)

# Pie chart to show the percentage of products based on their review categories
# We'll categorize the reviews into ranges
df['Review Category'] = pd.cut(df['Review'], bins=[0, 2.5, 4, 5], labels=['Low (<=2.5)', 'Medium (2.6 - 4)', 'High (>4)'])

fig5 = px.pie(df, names='Review Category', title='Review Distribution by Category')
st.plotly_chart(fig5)

st.write("Explore the best headphones available on Flipkart with these interactive data visualizations!")
