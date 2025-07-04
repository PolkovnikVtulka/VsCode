from selenium import webdriver
import time

def test_title_check():  # 🔹 Функция обязательно должна начинаться с `test_`
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org")
    time.sleep(2)
    
    title = driver.title
    print(title)  # 🔹 Это выведется благодаря флагу `-s`
    
    assert "Wikipedia" in title  # 🔹 Простая проверка, что в заголовке есть слово Wikipedia
    
    driver.quit()
