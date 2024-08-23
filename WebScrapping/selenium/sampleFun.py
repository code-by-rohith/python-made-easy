from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_driver():
    service = Service("C:/Users/rdroh/OneDrive/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    return driver


def open_url(driver, url):
    driver.get(url)

def click_element(driver, wait, by, value):
    element = wait.until(EC.element_to_be_clickable((by, value)))
    element.click()


def type_into_element(driver, wait, by, value, text):
    element = wait.until(EC.presence_of_element_located((by, value)))
    element.send_keys(text)


def navigate_back(driver, delay=3):
    time.sleep(delay)
    driver.back()

def main():
    driver = setup_driver()
    wait = WebDriverWait(driver, 40)

    # Perform actions using reusable functions
    open_url(driver, "https://www.google.com/")
    click_element(driver, wait, By.LINK_TEXT, "Gmail")
    click_element(driver, wait, By.LINK_TEXT, "Sign in")
    type_into_element(driver, wait, By.XPATH,
                      "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input",
                      "rdrohith02@gmail.com")
    click_element(driver, wait, By.ID, "identifierNext")

    navigate_back(driver, 3)
    navigate_back(driver, 3)
    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    main()
