from selenium import webdriver

# Создаем экземпляр WebDriver
driver = webdriver.Chrome()

# Открываем сайт
driver.get("https://www.python.org ")

# Делаем скриншот
driver.save_screenshot("screenshot.png")

# Закрываем браузер
driver.quit()