from selenium.webdriver.common.by import By



def login_qwerty (driver, by, login_locator, password_locator, login, password):
    login_field = driver.find_element(by, login_locator)
    login_field.send_keys(login)

    password_field = driver.find_element(by, password_locator)
    password_field.send_keys(password)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()