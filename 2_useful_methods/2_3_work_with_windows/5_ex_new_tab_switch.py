# Задание: переход на новую вкладку
# В этом задании после нажатия кнопки страница откроется в новой вкладке,
# нужно переключить WebDriver на новую вкладку и решить в ней задачу.

# Сценарий для реализации выглядит так:

# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ
# Если все сделано правильно и достаточно быстро
# (в этой задаче тоже есть ограничение по времени),
# вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.

import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    def calc(x):
        return str(log(abs(12 * sin(int(x)))))


    LINK = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(LINK)

    # Поиск кнопки
    button_start = browser.find_element(By.CSS_SELECTOR, '.btn')
    button_start.click()
    time.sleep(0.2)

    # Переключение вкладки
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

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
