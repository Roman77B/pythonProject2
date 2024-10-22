"""
Функция должна возвращать результат деления first на second, 
но когда в second записан 0 - возвращать строку 'Ошибка'.
"""
def divide(first, second):
    res = 'Ошибка' if second == 0 else first / second
    return res