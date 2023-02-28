# Задание: ждем нужный текст на странице

# Попробуем теперь написать программу,
# которая будет бронировать нам дом для отдыха по строго заданной цене.
# Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

# 1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# 2. Дождаться, когда цена дома уменьшится до $100
# (ожидание нужно установить не меньше 12 секунд)
# 3. Нажать на кнопку "Book"
# 4. Решить уже известную нам математическую задачу
# (используйте ранее написанный код) и отправить решение

# Чтобы определить момент, когда цена аренды уменьшится до $100,
# используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

# Если все сделано правильно и быстро, то вы увидите окно с числом.
# Отправьте его в качестве ответа на это задание.

import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    def calc(x):
        return str(log(abs(12 * sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Поиск бронирования
    book = browser.find_element(By.ID, "book")

    # Ожидание цены 100$
    prise = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book.click()

    # Поиск элемента х для вычисления
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    # Заполняем текстовое поле
    text_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", text_field)  # прокручиваем
    text_field.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()


finally:
    time.sleep(10)
    browser.quit()

