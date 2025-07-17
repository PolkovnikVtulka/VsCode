from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.python.org")

# Находим поле поиска по его имени
search_input = driver.find_element(By.NAME, "q")
search_input.send_keys("selenium\n")  # Вводим текст

time.sleep(5)
driver.quit()