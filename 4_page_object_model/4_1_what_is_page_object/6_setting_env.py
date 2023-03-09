# Подготовка окружения

# В этом модуле мы создадим с нуля полноценный тестовый проект,
# который будет являться вашим финальным заданием.
# Для этого будем использовать популярные в индустрии инструменты Git и GitHub,
# с которыми в общих чертах мы познакомились в предыдущем модуле.

# Добавлять изменения мы будем постепенно,
# чтобы в вашем репозитории была красивая история коммитов.
# Потому что именно так происходит написание промышленного кода,
# а наша задача в этом курсе — максимально приблизиться к этому процессу.

# Итак:

# Создайте отдельный публичный репозиторий с осмысленным названием на GitHub.
# Склонируйте его к себе на локальную машину.
# Добавьте туда файл conftest.py из предыдущего модуля.
# Убедитесь дополнительно, что там есть параметр для задания языка интерфейса, по умолчанию равный "en".

# Убедитесь что ни во вложенных папках, ни во внешних папках нет других файлов conftest.py,
# почему это важно смотри здесь: Conftest.py — конфигурация тестов.

# Добавьте в репозиторий файл requirements.txt из предыдущего модуля.
# Создайте пустой файл __init__.py, чтобы работали относительные импорты.
# Создайте файл test_main_page.py и добавьте в него тест из предыдущего модуля:

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     browser.get(link)
#     login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()

# Не забудьте активировать окружение, которое мы создали ранее.
# Опционально, можно создать для этого проекта новое виртуальное окружение для удобства.
# В таком случае убедитесь что вы установили туда все необходимые пакеты из requirements.txt.
# А еще не стоит добавлять файлы окружения в репозиторий
# и вообще в отслеживаемые — лишние файлы на GitHub это моветон.

# Убедитесь, что тест работает, с помощью следующей команды:
# pytest -v --tb=line --language=en test_main_page.py.

# Здесь и далее мы будем использовать эту команду для запуска.
# В этой команде мы использовали опцию PyTest --tb=line, которая указывает,
# что нужно выводить только одну строку из лога каждого упавшего теста.
# Так вам будет проще разобраться в том, как выглядят сообщения об ошибках.

# Добавьте все новые файлы в Git командой git add *
# Проверьте, что нужные файлы попали в планируемый коммит: git status

# Зафиксируйте изменения коммитом с осмысленным сообщением: git commit -m "write your message".

# По желанию добавьте описание репозитория с описанием вашего тестового проекта.
