# Методы-проверки в Page Object

# Давайте теперь автоматизируем другой тест-кейс и посмотрим на его примере,
# как делать методы-проверки.

# Допустим, нам нужно проверять такой сценарий:

# Открыть главную страницу
# Проверить, что есть ссылка, которая ведет на логин

# Для этого в классе MainPage нужно реализовать метод,
# который будет проверять наличие ссылки.
# Обычно все такие методы-проверки называются похожим образом,
# мы будем называть их should_be_(название элемента).

# Итак, в классе MainPage создайте метод should_be_login_link.

# Для первой пробы можно реализовать его самым примитивным образом:

# def should_be_login_link(self):
#     self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

# Сейчас мы намеренно сделали селектор неправильным,
# чтобы посмотреть, что именно выдаст тест, если поймает баг.
# Это хорошая практика: писать сначала красные тесты и только потом делать их зелеными.

# Добавляем в файл с тест-кейсами новый тест:

# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# Запустите получившийся тест:

# pytest -v --tb=line --language=en test_main_page.py

# Вывод об ошибке не очень понятный, правда?
# Разобраться, что именно пошло не так, довольно тяжело.
# Поэтому в следующем шаге нам нужно будет обработать исключение,
# которое выбрасывает WebDriver.

# В качестве ответа на данное задание напишите название исключения,
# которое вы получили в результате запуска теста.

# Познакомиться подробнее с работой с исключениями в Python вы можете в данной статье:
# http://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
