# Задание: отрицательные проверки

# Добавьте к себе в проект функции из предыдущего шага и реализуйте несколько простых тестов:

# test_guest_cant_see_success_message_after_adding_product_to_basket:
# Открываем страницу товара
# Добавляем товар в корзину
# Проверяем, что нет сообщения об успехе с помощью is_not_element_present

# test_guest_cant_see_success_message:
# Открываем страницу товара
# Проверяем, что нет сообщения об успехе с помощью is_not_element_present

# test_message_disappeared_after_adding_product_to_basket:
# Открываем страницу товара
# Добавляем товар в корзину
# Проверяем, что нет сообщения об успехе с помощью is_disappeared

# Запустите все три теста, и отметьте ниже верные утверждения для каждого теста.

# Важно! После того как пройдете это задание,
# те тесты, которые упали пометьте как XFail или skip,
# как это сделать мы разбирали в модуле 3: XFail: помечать тест как ожидаемо падающий.