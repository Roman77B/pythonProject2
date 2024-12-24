import threading
import time
import queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(0.5)

class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest == None:
                    table.guest = guest
                    table.guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            else: # у цикла for тоже есть else !!!)))
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал и ушел')
                    print(f'Стол {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty():
                        new_guest = self.queue.get()
                        table.guest = new_guest
                        table.guest.start()
                        print(f'{table.guest.name} вышел из очереди и сел за стол {table.number}')


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()