from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rombarkovsky.amocrm.ru")
driver.maximize_window()

# === ВВОДИМ ЛОГИН (username) ===
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
username_input.send_keys("test@example.com")  # ← подставь тестовый логин

# === НАЖИМАЕМ КНОПКУ "Продолжить" ===
continue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
)
continue_button.click()

# === ЖДЁМ ЗАГРУЗКУ ПОЛЯ ПАРОЛЯ ===
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
password_input.send_keys("testpassword")  # ← подставь тестовый пароль

# === НАЖИМАЕМ КНОПКУ "Войти" ===
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
)
login_button.click()

WebDriverWait(driver, 5)
driver.quit()
