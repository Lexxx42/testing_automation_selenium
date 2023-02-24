# Задание: загрузка файла
# В этом задании в форме регистрации требуется загрузить текстовый файл.

# Напишите скрипт, который будет выполнять следующий сценарий:

# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"
# Если все сделано правильно и быстро, вы увидите окно с числом.
# Отправьте полученное число в качестве ответа для этого задания.

import math
import time
from os import path, getcwd
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Ivan")

    sec_name = browser.find_element(By.NAME, "lastname")
    sec_name.send_keys("Petrov")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("asd@asd.asd")

    bio = browser.find_element(By.ID, "file")
    bio.send_keys(path.join(getcwd(), '7_bio.txt'))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
