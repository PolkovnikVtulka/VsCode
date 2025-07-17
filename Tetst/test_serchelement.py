from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

search_button = driver.find_element(By.ID, "searchInput")
search_button.send_keys("pythom\n")
time.sleep(5)



driver.get("https://www.youtube.com")
serch_you = driver.find_element(By.NAME, "search_query")
serch_you.send_keys("selenium tutorial")
serch_you.click()
time.sleep(5)