# Вы ведь уже догадались, что это ровно тоже самое, что делают @декораторы.:)

# Разрушаем ореол таинственности вокруг декораторов

# Вот так можно было записать предыдущий пример, используя синтаксис декораторов:

def my_shiny_new_decorator(a_function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку".
    # Она будет (что бы вы думали?..) обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.

    def the_wrapper_around_the_original_function():
        # Поместим здесь код, который мы хотим запускать ДО вызова
        # оригинальной функции
        print("Я - код, который отработает до вызова функции")

        # ВЫЗОВЕМ саму декорируемую функцию
        a_function_to_decorate()

        # А здесь поместим код, который мы хотим запускать ПОСЛЕ вызова
        # оригинальной функции
        print("А я - код, срабатывающий после")

    # На данный момент функция "a_function_to_decorate" НЕ ВЫЗЫВАЛАСЬ НИ РАЗУ

    # Теперь, вернём функцию-обёртку, которая содержит в себе
    # декорируемую функцию, и код, который необходимо выполнить до и после.
    # Всё просто!
    return the_wrapper_around_the_original_function


@my_shiny_new_decorator
def another_stand_alone_function():
    print("Оставь меня в покое")


another_stand_alone_function()
# выведет:
# Я - код, который отработает до вызова функции
# Оставь меня в покое
# А я - код, срабатывающий после

# Да, всё действительно так просто! decorator — просто синтаксический сахар для конструкций вида:

# another_stand_alone_function = my_shiny_new_decorator(another_stand_alone_function)



