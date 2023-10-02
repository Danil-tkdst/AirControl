from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Запускаем браузер и открываем страницу
browser = webdriver.Chrome()
browser.get("https://my.kaspersky.com/#/auth/layout/main")

# Проверяем, что заголовок страницы содержит слово "Kaspersky"
assert "Kaspersky" in browser.title

# Проверяем наличие полей ввода логина и пароля
username_input = browser.find_element_by_name("username")
password_input = browser.find_element_by_name("password")
assert username_input.is_displayed()
assert password_input.is_displayed()

# Вводим логин и пароль в соответствующие поля
username_input.send_keys("my_username")
password_input.send_keys("my_password")
password_input.send_keys(Keys.RETURN)

# Ждем загрузки страницы
browser.implicitly_wait(10)

# Проверяем, что на странице есть кнопка "My Account"
my_account_button = browser.find_element_by_xpath("//a[@class='m-account-link__btn js-m-account-link-btn']")
assert my_account_button.is_displayed()

# Закрываем браузер
browser.quit()