# Задание: работа с выпадающим списком
# Для этой задачи мы придумали еще один вариант капчи для роботов.
# Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

# Напишите код, который реализует следующий сценарий:

# Открыть страницу https://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"
# Если все сделано правильно и достаточно быстро
# (в этой задаче тоже есть ограничение по времени),
# вы увидите окно с числом.
# Отправьте полученное число в качестве ответа для этого задания.

# Когда ваш код заработает, попробуйте запустить его на
# странице https://suninjuly.github.io/selects2.html.
# Ваш код и для нее тоже должен пройти успешно.

# Подсказка: если вы получаете ошибку в духе
# "argument of type 'int' is not iterable",
# перепроверьте тип переменной, которую вы передаете в функцию поиска. Нужно передать строку!

import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'https://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.CSS_SELECTOR, '#num1').text)
    num2 = int(browser.find_element(By.CSS_SELECTOR, '#num2').text)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(num1 + num2))

    browser.find_element(By.CSS_SELECTOR, '.btn').click()  # Send submit

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
