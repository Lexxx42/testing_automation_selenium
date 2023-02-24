# Как вариант еще можно скрывать ненужный элемент
# browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)
# Еще в глобальном смысле мотнуть в самый верх или самый низ страницы можно и питоном для тега body
# from selenium.webdriver.common.keys import Keys
# browser.find_element_by_tag_name('body').send_keys(Keys.END) #или Home если наверх


# Задание на execute_script
# В данной задаче вам нужно будет снова преодолеть капчу для роботов
# и справиться с ужасным и огромным футером,
# который дизайнер всё никак не успевает переделать.

# Вам потребуется написать код, чтобы:

# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

# Если все сделано правильно и достаточно быстро
# (в этой задаче тоже есть ограничение по времени),
# вы увидите окно с числом.
# Отправьте полученное число в качестве ответа для этого задания.

# Для этой задачи вам понадобится использовать метод execute_script,
# чтобы сделать прокрутку в область видимости элементов, перекрытых футером.

import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    def calc(x):
        return str(log(abs(12 * sin(int(x)))))


    LINK = 'http://suninjuly.github.io/execute_script.html'
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
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)  # прокручиваем
    radio_button.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)  # прокручиваем
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
