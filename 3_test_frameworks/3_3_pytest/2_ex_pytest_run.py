# Попробуйте запустить ваши тесты из урока 3.2
# https://stepik.org/lesson/36285/step/13 с помощью PyTest.
# В выводе найдите последнюю строку, скопируйте её и отправьте в это задание.
# Отправьте текст, который находится между  === и ===.

# PS Обратите внимание - предупреждений (warnings) в вашем ответе быть не должно.

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAbs(unittest.TestCase):

    def test_registaration1(self):
        # Страница без бага
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(1)
        browser.get(link)

        # Kод, который заполняет обязательные поля
        firstname_input = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        firstname_input.send_keys('Ivanov')

        lastname_input = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        lastname_input.send_keys('Ivan')

        email_input = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        email_input.send_keys("test@mail.com")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        expected_text = "Congratulations! You have successfully registered!"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, expected_text, f"Expected {expected_text} got {welcome_text}")

    def test_registaration2(self):
        # Страница с багом.
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(1)
        browser.get(link)

        # Kод, который заполняет обязательные поля
        firstname_input = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        firstname_input.send_keys('Ivanov')

        lastname_input = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        lastname_input.send_keys('Ivan')

        email_input = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        email_input.send_keys("test@mail.com")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        expected_text = "Congratulations! You have successfully registered!"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, expected_text, f"Expected {expected_text} got {welcome_text}")


if __name__ == "__main__":
    unittest.main()

# ===== 1 failed, 1 passed in 10.21s ======
