# Цель: применить знания о рекурсии в решении задачи.
# Задача "Рекурсивное умножение цифр":
# Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа.
# Пункты задачи:
# 1. Напишите функцию get_multiplied_digits и параметр number в ней.
def get_multiplied_digits(number):
    # 2. Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
    str_number = str(number)
    #print(f'str_number={str_number}')
    # 3. Основной задачей будет отделение первой цифры в числе: создайте переменную first
    # и запишите в неё первый символ из str_number в числовом представлении(int).
    first = int(str_number[0])
    tmp = 0
    # 4. Возвращайте значение first * get_multiplied_digits(int(str_number[1:])).
    # Таким образом вы умножите первую цифру числа на результат работы
    # этой же функции с числом, но уже без первой цифры.
    # 4 пункт можно выполнить только тогда, когда длина str_number больше 1,
    # т.к. в противном случае не получится взять срез str_number[1:].
    # Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.
    if len(str_number) == 1:
        #print(f'first {first}')
        return first
    else:
        #print(f'first={first}, str_number={str_number}, int(str_number[1:])={int(str_number[1:])})')
        return first * get_multiplied_digits(int(str_number[1:]))

# Стек вызовов будет выглядеть следующим образом:
# get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3
# Пример результата выполнения программы:
# Исходный код:
result = get_multiplied_digits(40203)
print(result)
# Вывод на консоль:
# 24
#
# Примечания:
# При преобразовании строки(str) в число(int) первые нули убираются. int('00123') -> 123.
# Если возникает ошибка, рекомендуется пошагово отладить программу "жучком".
# Чаще всего ошибка заключается в бесконечной рекурсии или же в неверном обращении по индексу.