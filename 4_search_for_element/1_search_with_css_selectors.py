# Поиск элементов с помощью CSS-селекторов

# Ниже приведены части элементов HTML-страницы, по которым можно найти элемент:

# id
# tag
# значение атрибута
# name
# class

# Давайте откроем страницу http://suninjuly.github.io/cats.html и попробуем найти элемент,
# который содержит картинку с Котом-пулей (Bullet cat).

# Ниже приведён упрощенный кусок html-кода страницы:

# <div class="col-sm-4">
#   <div class="card mb-4 box-shadow">
#     <img id="bullet" name="bullet-cat" data-type="animal" class="card-img-top" src="images/bullet_cat.jpg">
#   </div>
# </div>

# Для начала мы попробуем искать элементы вручную с помощью консоли браузера,
# а в следующем уроке научимся писать код, который выполняет ту же задачу поиска.

# Поиск по id

# Какое везение! У элемента с нашей картинкой есть атрибут id="bullet",
# а значит, мы однозначно можем найти её с помощью селектора
# #bullet (знак # означает, что мы ищем по id со значением bullet).

# Можно проверить правильность подобранного селектора непосредственно в браузере в консоли разработчика.
# Откройте консоль разработчика и перейдите в ней на вкладку Elements.
# Затем нажмите ctrl+F и в открывшейся внизу поисковой строке введите селектор.
# Если селектор написан правильно, то вы увидите подсвеченный элемент на веб-странице,
# а также элемент будет подсвечен жёлтым цветом в html-коде.
# Еще в поисковой строке вы увидите количество найденных элементов.
# Желательно писать точные селекторы, которые позволяют найти ровно один элемент.
# В написании таких селекторов мы потренируемся в одной из следующих задач.

# Еще один способ открыть консоль разработчика в браузере:
# нажать правой кнопкой мыши на любой элемент страницы и выбрать пункт меню
# "Посмотреть код" (англ. "Inspect") в контекстном меню.
# При этом на вкладке Elements сразу будет подсвечен кусок HTML-кода, описывающий данный элемент.

# 1.jpg

# Поиск по tag

# Чтобы найти элемент по тегу, просто напишите название тега в поисковой строке,
# как мы делали это при поиске по id (только без знака #), например, h1.
# Поиск по h1 найдёт для нас элемент с названием страницы.
# Поиск по тегам не очень удобен, т.к. разработчики используют небольшое количество тегов для разметки страниц,
# и скорее всего, одному тегу будет соответствовать множество элементов.

# Поиск по значению атрибута

# Можно найти элемент, указав название атрибута и его значение.
# Например, можно переписать поиск по id в следующем виде [id="bullet"] вместо #bullet.

# Лучше использовать вариант с квадратными скобками при поиске значения атрибута для тех атрибутов,
# у которых нет собственных коротких команд поиска.
# Например, давайте найдем элемент h1 по значению его атрибута value: [value="Cat memes"].

# Поиск по name

# Этот вариант поиска является разновидностью поиска по значению атрибута и
# записывается так же: [name="bullet-cat"].
# Мы выделяем этот вариант потому что он довольно часто используется,
# а также выделяется как отдельный вид поиска элементов в Selenium WebDriver.

# Поиск по class

# Поиск по классу можно записать в виде [class="jumbotron-heading"],
# так как class тоже является атрибутом элемента.
# Но раз уж классы используются практически в каждой странице при задании стилей страниц,
# то для них также имеется свой короткий вариант поиска: .jumbotron-heading.
# То есть мы пишем значение класса и предваряем его точкой.

# Давайте рассмотрим важную разницу между двумя способами поиска по классу.
# Допустим, у элемента article задано больше одного класса,
# как на странице http://suninjuly.github.io/cats.html:

# <article id="moto" class="lead text-muted" title="one-thing" name="moto">
# If there's one thing that the internet was made for, it's funny cat memes.</article>

# Вариант [class="lead"] не найдет нам этот элемент,
# так как он ищет по точному совпадению.
# Чтобы найти элемент, нам нужно будет написать [class="lead text-muted"],
# порядок классов при этом важен. [class="text-muted lead"] — уже не найдет искомый элемент.

# Вариант .lead при этом позволит найти данный элемент,
# так как он ищет простое вхождение класса в элемент.
# Для уточнения селектора можно задать также оба класса,
# для этого нужно добавить второй класс к строке поиска без пробела и
# предварить его точкой: .lead.text-muted.
# Порядок классов в отличие от первого способа здесь не важен — .text-muted.lead
# так же найдет нужный элемент.
# Рекомендуем пользоваться вторым способом поиска классов, так как он является более гибким.

# Еще одно важное замечание.
# Поиск по классу чувствителен к регистру, то есть .Lead уже не найдет нужный элемент.

# В консоли браузера вы также можете искать по простому совпадению текста в HTML,
# например, запрос lead подсветит текст lead.
# Однако, не стоит пользоваться таким поиском для выбора элементов,
# так как он слишком общий и не может использоваться в качестве селектора.

# Мы рассмотрели разные варианты написания пути к элементу на странице,
# используя синтаксис CSS, т.е. научились писать CSS-селекторы.
# Слово "селектор" является буквальным переводом от английского слова selector.
# Selector в свою очередь происходит от глагола select, что переводится как "выбирать".

# Далее в этом уроке мы научимся искать элементы,
# комбинируя способы составления селекторов, рассмотренные в данном шаге.
