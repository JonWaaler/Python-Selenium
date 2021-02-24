from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com/")
time.sleep(1)
search = driver.find_element_by_name("q")
search.send_keys("black clover")
search.send_keys(Keys.RETURN)

time.sleep(3)
print("Shutting down webdriver...")
driver.quit()
