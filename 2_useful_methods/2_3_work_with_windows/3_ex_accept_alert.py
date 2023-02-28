# Задание: принимаем alert
# В этой задаче вам нужно написать программу,
# которая будет выполнять следующий сценарий:

# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом
# Если все сделано правильно и достаточно быстро
# (в этой задаче тоже есть ограничение по времени),
# вы увидите окно с числом.
# Отправьте полученное число в качестве ответа на это задание.


import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    def calc(x):
        return str(log(abs(12 * sin(int(x)))))


    LINK = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(LINK)

    # Поиск кнопки
    button_start = browser.find_element(By.CSS_SELECTOR, '.btn')
    button_start.click()

    # Принятие алерта
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(0.5)

    # Поиск элемента х для вычисления
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    # Заполняем текстовое поле
    text_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    text_field.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
