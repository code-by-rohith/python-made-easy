from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


service = Service('C:/Users/rdroh/OneDrive/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)


driver.get('https://github.com/code-by-rohith/')
time.sleep(3)
driver.find_element(By.XPATH,"""/html/body/div[1]/div[4]/main/div[1]/div/div/div[2]/div/nav/a[2]""").click()
time.sleep(2)
driver.find_element(By.XPATH, """/html/body/div[1]/div[4]/main/div[2]/div/div[2]/turbo-frame/div/div[2]/ul/li[1]/div[1]/div[1]/h3/a""").click()
time.sleep(2)
a=driver.find_element(By.XPATH,"""/html/body/div[1]/div[4]/div/main/turbo-frame/div/div/div/div[2]/div[1]/react-partial/div/div/div[2]/div[2]/div[1]/div[1]/div/span/input""")
a.send_keys('Welcome')
a.send_keys(Keys.ENTER)
time.sleep(500)
print("end")
driver.quit()
