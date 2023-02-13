# Поиск всех необходимых элементов с помощью find_elements

# Мы уже упоминали, что метод find_element возвращает только первый из всех элементов,
# которые подходят под условия поиска.
# Иногда возникает ситуация,
# когда у нас есть несколько одинаковых по сути объектов на странице,
# например, иконки товаров в корзине интернет-магазина.
# В тесте нам нужно проверить, что отображаются все выбранные для покупки товары.
# Для этого существует метод find_elements,
# которые в отличие от find_element вернёт список всех найденных элементов по заданному условию.
# Проверив длину списка, мы можем удостовериться,
# что в корзине отобразилось правильное количество товаров.
# Пример кода (код приведен только для примера,
# сайта fake-shop.com скорее всего не существует):

# # подготовка для теста
# # открываем страницу первого товара
# # данный сайт не существует, этот код приведен только для примера
# browser.get("https://fake-shop.com/book1.html")

# # добавляем товар в корзину
# add_button = browser.find_element(By.CSS_SELECTOR, ".add")
# add_button.click()

# # открываем страницу второго товара
# browser.get("https://fake-shop.com/book2.html")

# # добавляем товар в корзину
# add_button = browser.find_element(By.CSS_SELECTOR, ".add")
# add_button.click()

# # тестовый сценарий
# # открываем корзину
# browser.get("https://fake-shop.com/basket.html")

# # ищем все добавленные товары
# goods = browser.find_elements(By.CSS_SELECTOR, ".good")

# # проверяем, что количество товаров равно 2
# assert len(goods) == 2

# !Важно.
# Обратите внимание на важную разницу в результатах,
# которые возвращают методы find_element и find_elements.
# Если первый метод не смог найти элемент на странице,
# то он вызовет ошибку NoSuchElementException,
# которая прервёт выполнение вашего кода.
# Второй же метод всегда возвращает валидный результат:
# если ничего не было найдено,
# то он вернёт пустой список и ваша программа перейдет
# к выполнению следующего шага в коде.

import contextlib
import undetected_chromedriver as uc
# from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = uc.Chrome()
url = 'https://google.com'

try:
    browser.get(url)
    search = browser.find_element(By.CSS_SELECTOR, '[name="q"]')
    search.send_keys('ozon.ru')
    search.send_keys(Keys.RETURN)
    new_link = browser.find_element(By.PARTIAL_LINK_TEXT, "https://www.ozon.ru")
    new_link.click()
    goods = browser.find_elements(By.CSS_SELECTOR, ".n2e>.d4w>._4-a>button")
    print(goods)
finally:
    sleep(2)
    #browser.close()
    with contextlib.suppress(OSError):
        browser.quit()
