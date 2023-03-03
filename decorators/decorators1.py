# https://habr.com/ru/post/141411/

# Понимаем декораторы в Python'e, шаг за шагом. Шаг 1

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped


def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


@makebold
@makeitalic
def hello():
    return "hello habr"


print(hello())  ## выведет <b><i>hello habr</i></b>
