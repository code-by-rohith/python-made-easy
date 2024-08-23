from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service('C:/Users/rdroh/OneDrive/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://www.google.com/')
import  time
time.sleep(50)  # Keep the browser open for 5 seconds
driver.quit()
