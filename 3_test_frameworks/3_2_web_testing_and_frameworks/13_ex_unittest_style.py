# Задание: оформляем тесты в стиле unittest
# Попробуйте оформить тесты из первого модуля в стиле unittest.

# Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
# 1. Создайте новый файл
# 2. Создайте в нем класс с тестами,
# который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
# 3. Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
# 4. Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
# 5. Оформите финальные проверки в тестах в стиле unittest,
# например, используя проверочный метод assertEqual
# 6. Запустите получившиеся тесты из файла
# 7. Просмотрите отчёт о запуске и найдите последнюю строчку
# 8. Отправьте эту строчку в качестве ответа на это задание
# 9. Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте.
# Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё.
# Ловить исключения не надо (во всяком случае, здесь)!

# Это всё для иллюстрации того,
# что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения.

# Не удаляйте код после прохождения этого задания, он пригодится в следующем уроке.

import time
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
