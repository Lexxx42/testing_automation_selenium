# Декораторы — это просто pythonic-реализация паттерна проектирования «Декоратор».
# https://ru.wikipedia.org/wiki/%D0%94%D0%B5%D0%BA%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80_(%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F)
# В Python включены некоторые классические паттерны проектирования,
# https://ru.wikipedia.org/wiki/%D0%A8%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F#.D0.9E.D1.81.D0.BD.D0.BE.D0.B2.D0.BD.D1.8B.D0.B5
# такие как рассматриваемые в этой статье декораторы,
# или привычные любому пайтонисту итераторы.
# https://ru.wikipedia.org/wiki/%D0%98%D1%82%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80_(%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F)

# Конечно, можно вкладывать декораторы друг в друга, например так:

def bread(func):
    def wrapper():
        print("</------\>")
        func()
        print("<\______/>")

    return wrapper


def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")

    return wrapper


def sandwich(food="--ветчина--"):
    print(food)


sandwich()
# выведет: --ветчина--
sandwich = bread(ingredients(sandwich))
sandwich()

# выведет:
# </------\>
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>

# И используя синтаксис декораторов:
print('\n')


@bread
@ingredients
def sandwich(food="--ветчина--"):
    print(food)


sandwich()


# выведет:
# </------\>
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>

# Следует помнить о том, что порядок декорирования ВАЖЕН:

print('\n')
@ingredients
@bread
def sandwich(food="--ветчина--"):
    print(food)


sandwich()
# выведет:
# #помидоры#
# </------\>
# --ветчина--
# <\______/>
# ~салат~
