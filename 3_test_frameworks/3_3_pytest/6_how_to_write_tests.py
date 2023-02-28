# PyTest — как пишут тесты
# PyTest не требует написания дополнительных специфических конструкций в тестах,
# как того требует unittest.

# Мы уже увидели, что PyTest может запускать тесты, написанные в unittest-стиле.
# Перепишем наши тесты из test_abs_project.py в более простом формате,
# который также понимает PyTest. Назовём новый файл test_abs.py:

# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"

# def test_abs2():
#     assert abs(-42) == -42, "Should be absolute value of a number"

# Запустим тесты в этом файле:

# pytest test_abs.py
# Код тестов стал короче и читабельнее.

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_registaration1():
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
    assert welcome_text == expected_text, f"Expected {expected_text} got {welcome_text}"


def test_registaration2():
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
    assert welcome_text == expected_text, f"Expected {expected_text} got {welcome_text}"

# pytest 6_how_to_write_tests.py -v
