# Code Style: базовые принципы

# Имена переменных и функций

# Одним из самых важных аспектов читаемого кода является именование:
# будь то объявление переменных, описание функций, названия классов и так далее.

# Очень важно, чтобы все имена, которые вы присваивали сущностям,
# были осмысленными и отражали реальную суть этого объекта.

# Избегайте однобуквенных и бессмысленных названий типа var1, x, y, my_function, class2 и так далее.

# Идеальный код — самодокументируемый, к которому не нужны дополнительные пояснения.

# Если вы чувствуете, что вам хочется написать поясняющий комментарий,
# это повод переписать код так, чтобы комментарий не понадобился.

# Обычно внутри каждой компании есть дополнительные внутренние соглашения о том,
# как именовать переменные, но общие правила в индустрии примерно одинаковые.

# Функции пишутся через_нижнее_подчеркивание:
# def test_guest_can_see_lesson_name_in_lesson_without_course(self, driver):

# Классы пишут с помощью CamelCase:

# class TestLessonNameWithoutCourseForGuest():

# Константы пишут в стиле UPPERCASE:

# MAIN_PAGE = "/catalog"

# Максимальная простота кода

# Здесь нам на помощь приходят известные принципы написания кода
# DRY (Don't repeat yourself) и KISS (Keep it simple, stupid).

# Пишите максимально простой код везде, где это возможно.

# Не используйте переусложненных конструкций без большой необходимости
# (поменьше лямбда-выражений, map и разной другой магии).

# Если кусок кода можно заменить конструкцией более простой для понимания — замените.

# Пишите максимально линейный код, где это возможно, это проще для восприятия.

# Избегайте большой вложенности блоков кода, такие конструкции тяжело читать.

# Если можно вынести повторяющуюся логику куда-то, выносите, не повторяйтесь.

# По возможности пишите явный код вместо неявного. Чем меньше магии "под капотом", тем лучше.
import this
