# Дополнительное практическое задание по модулю*
# Универсальное решение для подсчёта суммы всех чисел и длин всех строк
# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то);
# Все строки (не важно, являются они ключами или значениям или ещё чем-то).

cnt = 0

def calculate_structure_sum(*args):
    global cnt
    for a in args:
        if type(a) is int:
            cnt += a
        elif type(a) is str:
            cnt += len(a)
        elif isinstance(a, dict):
            calculate_structure_sum(a.items())
        else:
            calculate_structure_sum(*a)
        # print(type(a), a, f'cnt={cnt}') # отладка
    return cnt

data_structure = [
  [1, 2, 3],                                # 6
  {'a': 4, 'b': 5},                         # 11
  (6, {'cube': 7, 'drum': 8}),              # 29
  "Hello",                                  # 5
  ((), [{(2, 'Urban', ('Urban2', 35))}])    # 48
]

result = (calculate_structure_sum(*data_structure))
print(result)