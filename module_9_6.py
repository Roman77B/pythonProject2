# Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.
# Задача:
# Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
# при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
# Пункты задачи:
# Напишите функцию-генератор all_variants(text).
# Опишите логику работы внутри функции all_variants.
# Вызовите функцию all_variants и выполните итерации.

# Вот такую конструкцию Яндек-Нейро предложил
def all_variants(text):
     length = len(text)
     for x in range(length):
         for y in range(x, length):
             yield text[x:y + 1]

# Пример работы функции:
a = all_variants("abc")
for i in a:
    print(i)
# Вывод на консоль:
# a
# b
# c
# ab
# bc
# abc
