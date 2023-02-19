# Задание: кликаем по checkboxes и radiobuttons (капча для роботов)

# Продолжим использовать силу роботов 🤖 для решения повседневных задач.
# На данной странице мы добавили капчу для роботов,
# то есть тест, являющийся простым для компьютера, но сложным для человека.

# Ваша программа должна выполнить следующие шаги:

# Открыть страницу https://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.
# Для этой задачи вам понадобится использовать атрибут .text для найденного элемента.
# Обратите внимание, что скобки здесь не нужны:

# x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
# x = x_element.text
# y = calc(x)
# Атрибут text возвращает текст,
# который находится между открывающим и закрывающим тегами элемента.
# Например, text для данного элемента <div class="message">У вас новое сообщение.</div>
# вернёт строку: "У вас новое сообщение".

# Используйте функцию calc(),
# которая рассчитает и вернет вам значение функции,
# которое нужно ввести в текстовое поле.
# Не забудьте добавить этот код в начало вашего скрипта:

# import math

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

# Если все сделано правильно и достаточно быстро
# (в этой задаче тоже есть ограничение по времени),
# вы увидите окно с числом. Скопируйте его в поле ниже.

import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    def calc(x):
        return str(log(abs(12 * sin(int(x)))))


    LINK = 'https://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(LINK)

    # Поиск значения переменной
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    # Заполняем текстовое поле
    text_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    text_field.send_keys(y)

    # Активация чекбокса
    check_box = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    check_box.click()
    # Активация радиобатона
    radio_button = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio_button.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
