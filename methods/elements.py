from selenium.webdriver.common.by import By

def click_element(driver, by, locator):
    element = driver.find_element(by, locator).click()
    
    
def send_keys_element(driver, by, locator, text):
    element = driver.find_element(by, locator)
    element.send_keys(text)