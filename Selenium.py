from selenium import webdriver
import time
PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www12.9anime.to/home")
time.sleep(5)
print("Shutting down webdriver...")
driver.quit()
