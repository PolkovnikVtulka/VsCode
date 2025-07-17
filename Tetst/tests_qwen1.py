from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_qwen1():
    # Создаем экземпляр WebDriver
    driver = webdriver.Chrome()

    try:
        # Открываем сайт
        driver.get("https://www.wikipedia.org/ ")

        # Явное ожидание появления кнопки "English"
        wait = WebDriverWait(driver, 10)
        english_button = wait.until(EC.element_to_be_clickable((By.ID, "js-link-box-en")))

        # Кликаем по кнопке
        english_button.click()

        # Явное ожидание загрузки новой страницы
        wait.until(EC.title_contains("Wikipedia"))

        # Проверяем заголовок страницы
        expected_title = "Wikipedia, the free encyclopedia"
        actual_title = driver.title

        assert actual_title == expected_title, f"Ошибка: ожидалось '{expected_title}', получено '{actual_title}'"
        print("Тест пройден!")

    finally:
        # Закрываем браузер
        driver.quit()