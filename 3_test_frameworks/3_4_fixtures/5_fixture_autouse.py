# Автоиспользование фикстур
# При описании фикстуры можно указать дополнительный параметр autouse=True,
# который укажет, что фикстуру нужно запустить для каждого теста даже без явного вызова:

# test_fixture_autouse.py

# Попробуйте запустить этот код и увидите,
# что для каждого теста фикстура подготовки данных выполнилась без явного вызова.
# Нужно быть аккуратнее с этим параметром, потому что фикстура выполняется для всех тестов.
# Без явной необходимости автоиспользованием фикстур лучше не пользоваться.

# Итог

# Вспомогательные функции — это очень мощная штука,
# которая решает много проблем при работе с автотестами.
# Основной плюс в том, что их удобно использовать в любых тестах без дублирования лишнего кода.

# Дополнительные материалы про фикстуры, которые мы настоятельно советуем почитать, приведены ниже:

# https://habr.com/ru/company/yandex/blog/242795/

# https://docs.pytest.org/en/stable/fixture.html
