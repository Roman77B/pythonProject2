# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".
# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
# Пример результата выполнения программы:
# Пример выполняемого кода:
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
# # __str__
# print(h1)
# print(h2)
# # __len__
# print(len(h1))
# print(len(h2))
# Вывод на консоль:
# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК Акация, кол-во этажей: 20
# 10
# 20

# Создайте новый класс House
# Создайте инициализатор для класса House, который будет задавать атрибут этажности self.numberOfFloors = 0
# Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут numberOfFloors на параметр floors и выводить в консоль numberOfFloors
# Полученный код напишите в ответ к домашнему заданию

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def setNewNumberOfFloors(self, floors):
        self.number_of_floors = floors  # number_of_floors
        print (self.number_of_floors)

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(str(h1))
print(str(h2))
print(len(h1))
print(len(h2))