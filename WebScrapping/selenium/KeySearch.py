from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service('C:/Users/rdroh/OneDrive/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.co.in//')

wait = WebDriverWait(driver, 20)


search = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')))
search.send_keys('python online compiler')
search.send_keys(Keys.ENTER)



first_result = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[3]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/span/a""")))
first_result.click()

button = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[2]/div[6]/div[4]/div[1]/div[2]/button[5]""")))
button.click()
time.sleep(100)

# Quit the driver
driver.quit()
