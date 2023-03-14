# Задание: setup

# Ниже вы найдете небольшой пазл из строк кода, которые нужно собрать в правильном порядке.

# Мы хотим обернуть тест-кейс test_guest_cant_see_success_message
# в тестовый класс TestAddToBasketFromProductPage с подготовкой данных,
# точно так же как в примере из предыдущего шага.

# Расположите элементы списка в правильном порядке

# @pytest.mark.add_to_basket
# class TestAddToBasketFromProductPage(object):
# @pytest.fixture(scope="function", autouse=True)
# def setup(self):
# self.product = ProductFactory(title="Best book created by robot")
# self.link = self.product.link
# yield
# self.product.delete()
# def test_guest_cant_see_success_message(self, browser):
# page = ProductPage(browser, self.link)
