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

link = 'https://stepik.org/lesson/236895/step/1'


def test_login(browser):
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
