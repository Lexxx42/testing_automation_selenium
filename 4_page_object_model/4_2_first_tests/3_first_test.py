# Первый тест на основе Page Object

# Ура, первый прототип страницы мы уже реализовали! Давайте теперь перепишем тест с помощью Page Object:

# 1. Откройте файл с вашим тестом test_main_page.py

# 2. В самом верху файла нужно импортировать класс, описывающий главную страницу:

# from .pages.main_page import MainPage
# 3. Теперь преобразуем сам тест в test_main_page.py:

# from .pages.main_page import MainPage

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

# 4. Убедитесь, что тест проходит, запустив его все той же командой:

# pytest -v --tb=line --language=en test_main_page.py

# 5. Добавьте изменения и сделайте коммит (с осмысленным сообщением!)

# Теперь наш тест почти полностью написан в модном стиле Page Object!
# Почему почти — узнаете в следующих шагах.
