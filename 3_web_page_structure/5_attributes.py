# Подробнее об атрибутах (data-атрибуты)

# Как мы уже говорили, некоторые атрибуты напрямую не влияют на отображение элемента на страницах.
# О некоторых таких важных атрибутах мы уже поговорили в шаге 3 (например, id).

# А еще список атрибутов можно расширять: это значит,
# что разработчик может создать свой собственный атрибут и присвоить ему любые значения.
# Что это значит для тестировщика?
# Это значит, что можно договориться с разработчиками о специальном атрибуте,
# который вы будете использовать в своих тестах для поиска нужных элементов
# и который не будет изменяться при исправлении верстки сайта.
# Это добавит стабильности вашим тестам. Правда, есть несколько ограничений:

# веб-сайт должен использовать стандарт HTML5 (большинство современных сайтов соответствует этому требованию)
# использовать можно только латинские буквы, и символы дефис (-), двоеточие (:) и подчёркивание (_)

# Также принято названия таких атрибутов начинать со слова: "data", например, "data-button".

# Что еще важно знать про атрибуты элементов?

# Некоторые атрибуты являются универсальными,
# они могут относиться к любому тегу и любому типу элементов.
# Например, hidden (т.е. скрытым) можно сделать любой элемент.
# Некоторые же атрибуты ассоциированы строго с определенным тегом, например, для картинки,
# которая задается тегом img, обязательно нужно указывать атрибут src.

# Если вы собираетесь в дальнейшем работать с автоматизацией тестирования веб-продуктов,
# то вам будет очень полезно изучить HTML более детально.
# Вы сможете быстро подбирать нужные селекторы,
# с первого взгляда на HTML-разметку будете видеть что <a> - это ссылка,
# <p> - текст, а <ul> - ненумерованный (маркированный) список.
# Но это большая и широкая тема, которая заслуживает отдельного курса
# (можно проходить такие курсы самостоятельно, например, https://stepik.org/course/38218/).

# Образовательная рекомендация: если вы не совсем понимаете,
# что означает тег или атрибут элемента, попробуйте погуглить.
# Каждый кусочек этих знаний так или иначе поможет вам в будущем.

# Для закрепления знаний про атрибуты предлагаем вам следующее задание: сопоставьте атрибут с его описанием.
# Не все из этих атрибутов были упомянуты ранее, так что не стесняйтесь пользоваться любым поисковиком :)

# id - универсальный атрибут, представляет собой уникальный идентификатор элемента на странице
# title - универсальный атрибут, задаёт всплывающую подсказку по наведению на элемент
# href - для тега <a> задаёт адрес ссылки
# target - для тега <a> указывает, как именно открыть ссылку: в текущем окне или в новом
# src - для тега <img> задает ссылку на источник изображения
