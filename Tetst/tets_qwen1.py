from selenium import webdriver
import time

def test_qwen1():
    driver = webdriver.Chrome()
    
    driver.get("https://www.wikipedia.org/")
    time.sleep(2)
    
    english_button = driver.find_element("id", "js-link-box-en")
    english_button.click()
    time