from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from random import randint
import time
import os

load_dotenv()

driver = webdriver.Chrome()
driver.get("https://twitter.com/i/flow/login")
time.sleep(randint(5, 10))

# input username
input_box = driver.find_element(by=By.TAG_NAME, value="input")
input_box.send_keys(f"{os.getenv('TWITTER_USERNAME')}")
input_box.send_keys(Keys.RETURN)
time.sleep(randint(5, 10))

# input password
input_box = driver.find_element(by=By.XPATH, value="//input[@type='password']")
input_box.send_keys(f"{os.getenv('TWITTER_PASSWORD')}")
input_box.send_keys(Keys.RETURN)
time.sleep(randint(5, 10))

# accept cookies
accept_cookies = driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Accept all cookies')]")
accept_cookies.click()

driver.quit()
