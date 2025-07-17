from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_qwen1():
    driver = webdriver.Chrome()

    try:
        # Открываем сайт
        driver.get("https://www.wikipedia.org/ ")

        # Создаем объект WebDriverWait
        wait = WebDriverWait(driver, 10)

        # Ждем, пока кнопка "English" станет кликабельной
        english_button = wait.until(EC.element_to_be_clickable((By.ID, "js-link-box-en")))

        # Кликаем по кнопке
        english_button.click()

        # Ждем, пока заголовок страницы будет содержать "Wikipedia"
        wait.until(EC.title_contains("Wikipedia"))

        # Проверяем заголовок страницы
        assert driver.title == "Wikipedia", f"Ошибка: ожидалось 'Wikipedia', получено '{driver.title}'"
        print("Тест пройден!")

    finally:
        # Закрываем браузер
        driver.quit()
