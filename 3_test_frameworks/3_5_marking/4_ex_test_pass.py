# Задание: пропуск тестов

# Изучите самостоятельно документацию про маркировку xfail.

# Найдите там параметр, который в случае неожиданного прохождения теста,
# помеченного как xfail, отметит в отчете этот тест как упавший.
# Пометьте таким образом первый тест из этого тестового набора.

#test_xfail.py

# https://docs.pytest.org/en/latest/reference/reference.html#pytest.mark.xfail

# Запустите полученные тесты.
# Обратите внимание на статус прогона тестов.
# Найдите последнюю строчку с итогами запуска,
# скопируйте текст между символами === и отправьте его в качестве ответа на это задание.

# pytest -s -rx -v .\test_xfail.py

#  1 failed, 1 skipped, 1 xfailed in 0.06s
