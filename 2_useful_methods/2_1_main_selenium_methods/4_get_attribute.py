# Задание: поиск сокровища с помощью get_attribute
# В данной задаче вам нужно с помощью роботов решить ту же математическую задачу,
# как и в прошлом задании.
# Но теперь значение переменной х спрятано в "сундуке",
# точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

# Ваша программа должна:

# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

# Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи.

# Если все сделано правильно и достаточно быстро
# (в этой задаче тоже есть ограничение по времени),
# вы увидите окно с числом.
# Скопируйте его в поле ниже и нажмите кнопку "Submit", чтобы получить баллы за задание.

import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    def calc(x):
        return str(log(abs(12 * sin(int(x)))))


    LINK = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(LINK)

    # Поиск значения переменной
    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = x_element.get_attribute("valuex")
    y = calc(x)

    # Заполняем текстовое поле
    text_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    text_field.send_keys(y)

    # Активация чекбокса
    check_box = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    check_box.click()

    # Активация радиобатона
    radio_button = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio_button.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
