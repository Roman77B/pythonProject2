# Задание: Декораторы в Python
# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
# Задание:
# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое",
# если результат 1ой функции будет простым числом и "Составное" в противном случае.
# Пример:
# result = sum_three(2, 3, 6)
# print(result)
#
def is_prime(func):
    def wrp(*args,**kwargs):

        # Функция определения простого числа
        import math
        def is_prime_num(number):
            # список простых чисел начинается с 2, всё остальное можно сразу отмести [1](https://ru.hexlet.io/qna/python/questions/kakaya-funktsiya-nuzhna-dlya-nahozhdeniya-prostogo-chisla-v-python)
            if number <= 1:
                return False
            number_sqrt = int(math.sqrt(number))
            divisors = range(2, (number_sqrt + 1))
            # Если число не простое, то в отрезке от 1 до квадратного корня числа, точно будут его делители [1](https://ru.hexlet.io/qna/python/questions/kakaya-funktsiya-nuzhna-dlya-nahozhdeniya-prostogo-chisla-v-python)
            for element in divisors:
                if number % element == 0:
                    return False
            return True

        summ = func(*args, **kwargs)

        if is_prime_num(summ):
            print("Простое")
        else:
            print("Составное")

        return summ

    return wrp

@is_prime
def sum_three(x, y, z):
    return x + y + z

result = sum_three(2, 3, 6)
print(result)

# Результат консоли:
# Простое
# 11
#
# Примечания:
# Не забудьте написать внутреннюю функцию wrapper в is_prime
# Функция is_prime должна возвращать wrapper
# @is_prime - декоратор для функции sum_three