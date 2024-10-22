from math import inf
"""
Функция должна возвращать результат деления first на second, 
но когда в second записан 0 - возвращать бесконечность.
"""
def divide(first, second):
    res = inf if second == 0 else first / second
    return res