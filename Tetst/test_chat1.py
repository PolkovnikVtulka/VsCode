from selenium import webdriver
import time 

driver = webdriver.Chrome()
driver.get("https://www.python.org")
time.sleep(5)
driver.quit()