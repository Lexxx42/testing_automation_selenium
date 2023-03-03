# Задание: авторизация на сайте

# Для следующей задачи вам необходимо авторизоваться на stepik со своим логином и паролем.
# Пожалуйста, будьте внимательны и не добавляйте свои логин и пароль в публичные репозитории на GitHub.

# Ваша задача -- реализовать автотест со следующим набором действий:

# открыть в Chrome урок по ссылке https://stepik.org/lesson/236895/step/1
# авторизоваться со своими логином и паролем
# дождаться того, что поп-апа с авторизацией больше нет
# После того как авторизация успешно пройдет, переходите к следующему шагу.

import os
import time
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

load_dotenv()

LOGIN = os.getenv('LOGIN')
PASS = os.getenv('PASWD')

LINK = 'https://stepik.org/lesson/236895/step/1'


def test_login(browser):
    browser.implicitly_wait(5)
    browser.get(LINK)
    browser.find_element(By.CSS_SELECTOR, '#ember33').click()

    login_email = browser.find_element(By.CSS_SELECTOR, '#id_login_email')
    login_email.send_keys(LOGIN)

    login_pass = browser.find_element(By.CSS_SELECTOR, '#id_login_password')
    login_pass.send_keys(PASS)

    browser.find_element(By.CSS_SELECTOR, '.sign-form__btn').click()

    time.sleep(10)
