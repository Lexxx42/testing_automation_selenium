# Задание: параметризация тестов

# Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение.
# Мы смогли локализовать несколько url-адресов задач,
# где появляются кусочки сообщений.

# Ваша задача — реализовать автотест со следующим сценарием действий:

# открыть страницу
# авторизоваться на странице со своим логином и паролем (см. предыдущий шаг)
# ввести правильный ответ (поле перед вводом должно быть пустым)
# нажать кнопку "Отправить"
# дождаться фидбека о том, что ответ правильный
# проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
# Опциональный фидбек — это текст в черном поле, как показано на скриншоте:

# Правильным ответом на задачу в заданных шагах является число:

# import time
# import math

# answer = math.log(int(time.time()))

# Используйте маркировку pytest для параметризации
# и передайте в тест список ссылок в качестве параметров:

# https://stepik.org/lesson/236895/step/1
# https://stepik.org/lesson/236896/step/1
# https://stepik.org/lesson/236897/step/1
# https://stepik.org/lesson/236898/step/1
# https://stepik.org/lesson/236899/step/1
# https://stepik.org/lesson/236903/step/1
# https://stepik.org/lesson/236904/step/1
# https://stepik.org/lesson/236905/step/1

# Используйте осмысленное сообщение об ошибке в проверке текста,
# а также настройте нужные ожидания, чтобы тесты работали стабильно.

# В упавших тестах найдите кусочки послания.
# Тест должен падать, если текст в опциональном фидбеке не совпадает со строкой "Correct!"
# Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание.

# Важно! Чтобы пройти это задание,
# дополнительно убедитесь в том, что у вас установлено правильное локальное время (https://time.is/ru/).
# Ответ для каждой задачи нужно пересчитывать отдельно, иначе они устаревают.


import os
import time
import pytest
from math import log
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

LOGIN = os.getenv('LOGIN')
PASS = os.getenv('PASWD')

link = ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1']


@pytest.mark.parametrize('link', link)
def test_login(browser, link):
    browser.get(link)
    time.sleep(3)
    login_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#ember33'))
    )
    login_button.click()

    login_email = browser.find_element(By.CSS_SELECTOR, '#id_login_email')
    login_email.send_keys(LOGIN)

    login_pass = browser.find_element(By.CSS_SELECTOR, '#id_login_password')
    login_pass.send_keys(PASS)

    browser.find_element(By.CSS_SELECTOR, '.sign-form__btn').click()
    time.sleep(5)

    if len(do_again := browser.find_elements(By.CSS_SELECTOR, '.again-btn')) > 0:
        do_again[0].click()
        time.sleep(1)

    text_area = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea'))

    )

    text_area.clear()
    time.sleep(2)
    text_area.send_keys(str(log(int(time.time()))))

    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission'))
    )
    submit_button.click()

    time.sleep(2)

    tip = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))
    )
    time.sleep(2)
    tip_text = tip.text
    assert tip_text in 'Correct!'
