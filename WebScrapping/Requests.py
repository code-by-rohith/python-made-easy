import requests
url='https://googlechromelabs.github.io/chrome-for-testing/'
r=requests.get(url)
print(r.status_code)
print(r.text)
