# Плагины и перезапуск тестов

# Для PyTest написано большое количество плагинов,

# https://docs.pytest.org/en/latest/explanation/flaky.html#plugins

# то есть дополнительных модулей, которые расширяют возможности этого фреймворка.
# Полный список доступных плагинов доступен здесь.

# https://docs.pytest.org/en/latest/reference/plugin_list.html

# Рассмотрим еще одну проблему, с которой вы обязательно столкнетесь,
# когда будете писать end-to-end тесты на Selenium.
# Flaky-тесты или "мигающие" авто-тесты, т.е. такие тесты,
# которые по независящим от нас внешним обстоятельствам или из-за трудновоспроизводимых багов,
# могут иногда падать, хотя всё остальное время они проходят успешно.

# Это может происходить в момент прохождения тестов из-за одновременного обновления сайта,
# из-за сетевых проблем или странных стечений обстоятельств.

# Конечно, надо стараться исключать такие проблемы и искать причины возникновения багов,
# но в реальном мире бывает, что это требует слишком много усилий.

# Поэтому мы будем перезапускать упавший тест, чтобы еще раз убедиться,
# что он действительно нашел баг, а не упал случайно.

# Это сделать очень просто.
# Для этого мы будем использовать плагин pytest-rerunfailures.

# Сначала установим плагин в нашем виртуальном окружении.
# После установки плагин будет автоматически найден PyTest,
# и можно будет пользоваться его функциональностью без дополнительных изменений кода:

# pip install pytest-rerunfailures

# Чтобы указать количество перезапусков для каждого из упавших тестов,
# нужно добавить в командную строку параметр:

# "--reruns n",
# где n — это количество перезапусков.

# Если при повторных запусках тесты пройдут успешно,
# то и прогон тестов будет считаться успешным.
# Количество перезапусков отображается в отчёте,
# благодаря чему можно позже анализировать проблемные тесты.

# Дополнительно мы указали параметр "--tb=line",
# чтобы сократить лог с результатами теста.
# Можете почитать подробнее про настройку вывода в документации PyTest:

# https://docs.pytest.org/en/stable/how-to/usage.html#modifying-python-traceback-printing

# pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py

# Давайте напишем два теста: один из них будет проходить, а другой — нет.
# Посмотрим, как выглядит перезапуск.

# test_rerun.py:

# link = "http://selenium1py.pythonanywhere.com/"
#
# def test_guest_should_see_login_link_pass(browser):
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#login_link")
#
# def test_guest_should_see_login_link_fail(browser):
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#magic_link")

# Мы увидим сообщение: "1 failed, 1 passed, 1 rerun in 9.20s",
# то есть упавший тест был перезапущен, но при втором запуске тоже упал.
# Если бы во второй раз мигающий тест все-таки прошёл успешно, то мы бы увидели сообщение:
# "2 passed, 1 rerun in 9.20s",
# и итоговый результат запуска всех тестов считался бы успешным.