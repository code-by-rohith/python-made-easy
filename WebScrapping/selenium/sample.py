from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

service = Service("C:/Users/rdroh/OneDrive/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com/")
wait = WebDriverWait(driver, 40)

typ1 = wait.until(EC.presence_of_element_located((By.ID, "APjFqb")))
typ1.send_keys("Coimbatore Institute Of Technology: Home")
typ1.send_keys(Keys.ENTER)

search = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[13]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/span/a")))
search.click()

search2 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div/div/div/div/div/a")))
search2.click()

try:
    cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cookie-policy']//a[contains(text(), 'I Understand')]")))
    cookie_button.click()
    print("Cookie button clicked.")
except:
    print("Cookie button not found.")
    pass

typ = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/section/div/div/div[1]/div/div/div/div/ul/li[4]/button")))
typ.click()

search3 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/header/div[1]/div[1]/div/div[2]/ul/li[3]/a")))
search3.click()

search4 = wait.until(EC.element_to_be_clickable((By.ID, "nav_top_left_12")))
search4.click()



time.sleep(7)
driver.back()
time.sleep(3)
driver.back()
time.sleep(5)
driver.quit()
