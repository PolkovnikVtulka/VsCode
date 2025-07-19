from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from methods.auth_methods import login_qwerty


def test_login_amocrm():
    driver = webdriver.Chrome()
    driver.get("https://rombarkovsky.amocrm.ru")

    # Вводим логин и пароль
    login_qwerty(
        driver,
        by=By.NAME,
        login_locator="USER_LOGIN",
        password_locator="USER_HASH",
        login="rombarkovsky@team.amocrm.com",         # <-- ЗАМЕНИ НА РЕАЛЬНЫЙ ЛОГИН
        password="Patrik200116%"            # <-- ЗАМЕНИ НА РЕАЛЬНЫЙ ПАРОЛЬ
    )

    # Подожди немного (в будущем — заменим на явные ожидания)
    time.sleep(3)

    # Проверка — пример: убедиться, что URL поменялся
    assert "https://www.kommo.com/" not in driver.current_url, "Похоже, вход не удался"

    driver.quit()