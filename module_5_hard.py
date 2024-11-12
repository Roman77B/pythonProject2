# Дополнительное практическое задание по модулю: "Классы и объекты."
# Задание "Свой YouTube":
# Всего будет 3 класса: UrTube, Video, User.
# Общее ТЗ:
# Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео,
# авторизации и регистрации пользователя и т.д.
# Подробное ТЗ:
# Каждый объект класса User должен обладать следующими атрибутами и методами:
#   Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
# Каждый объект класса Video должен обладать следующими атрибутами и методами:
#   Атрибуты: title(заголовок, строка), duration(продолжительность, секунды),
#   time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
#   Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
#   Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users
#   с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного.
#   Помните, что password передаётся в виде строки, а сравнивается по хэшу.
#   Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
#   если пользователя не существует (с таким же nickname).
#   Если существует, выводит на экран: "Пользователь {nickname} уже существует".
#   После регистрации, вход выполняется автоматически.
#   Метод log_out для сброса текущего пользователя на None.
#   Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
#   если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
#   Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео,
#   содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует
#   в строке 'Urban the best' (не учитывать регистр).
#   Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
#   то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
#   После текущее время просмотра данного видео сбрасывается.
#   Для метода watch_video так же учитывайте следующие особенности:
#   Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
#   Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
#   В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
#   Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре,
#   т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
#   После воспроизведения нужно выводить: "Конец видео"

from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname        # имя пользователя, строка
        self.password = password        # password в хэшированном виде, число
        self.age = age                  # возраст, число

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title              # заголовок, строка
        self.duration = duration        # продолжительность, секунды
        self.time_now = time_now        # секунда остановки (изначально 0)
        self.adult_mode = adult_mode    # ограничение по возрасту, bool (False по умолчанию)

class UrTube:
    def __init__(self):
        self.users = []                 # список объектов User
        self.videos = []                # список объектов Video
        self.current_user = None        # текущий пользователь, User

    # Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users
    # с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного.
    # Помните, что password передаётся в виде строки, а сравнивается по хэшу.
    def log_in(self, nickname, password):
        # print(f'пришли в log_in {nickname} {password}')
        for u in self.users:
            if u.nickname == nickname and u.password == password:
                # print('Пользователь найден')
                self.current_user = u
                break

    #   Метод register, который принимает три аргумента: nickname, password, age,
    #   и добавляет пользователя в список, если пользователя не существует (с таким же nickname).
    #   Если существует, выводит на экран: "Пользователь {nickname} уже существует".
    #   После регистрации, вход выполняется автоматически.
    def register(self, nickname, password, age):
        usrs = []
        for u in self.users:
            usrs.append(u.nickname)
        if nickname not in usrs:
            self.users.append(usr := User(nickname, hash(password), age))
            # print(f'сейчас добавился пользователь {usr.nickname}')
            self.log_in(usr.nickname, usr.password)
        else:
            print(f'Пользователь {nickname} уже существует')

    # Метод log_out для сброса текущего пользователя на None.
    def log_out(self):
        self.current_user = None

    # Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
    # если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
    def add(self, *args):
        for v in args:
            if isinstance(v, Video):
                if len(self.videos) == 0:   # print(f'Добавили первое видео {v.title}')
                    self.videos.append(v)
                    titles = {v.title}      # вспомог. множество назв-й видео, чтобы не добавлять одинаковые названия
                else:
                    if v.title not in titles:
                        self.videos.append(v)
                        titles.add(v.title)

    # Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео,
    # содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует
    # в строке 'Urban the best' (не учитывать регистр).
    def get_videos(self, fnd_str):
        titles_nm = []
        titles_fnd = []
        for a in self.videos:
            titles_nm.append(a.title)
        # print('Отладка1', titles_nm)
        for titles_nm_sub in titles_nm:
            # print('Отладка2', titles_nm_sub)
            if fnd_str.lower() in titles_nm_sub.lower():
                # print(f'Отладка 3 нашли "{fnd_str.lower()}" в строке "{titles_nm_sub.lower()}"')
                titles_fnd.append(titles_nm_sub)
                # print(f'Отладка 4 добавили "{titles_nm}" в список поиска "{titles_fnd}"')

        return(titles_fnd)

    #   Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
    #   то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
    #   После текущее время просмотра данного видео сбрасывается.
    #   Для метода watch_video так же учитывайте следующие особенности:
    #   Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
    #   Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
    #   В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
    #   Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре,
    #   т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
    #   После воспроизведения нужно выводить: "Конец видео"
    def watch_video (self, v_nm):
        # titles_nm = []
        for v in self.videos:
            # titles_nm.append(a.title)

            if v_nm in v.title:
                if self.current_user == None:  # текущий пользователь, User
                    print("Войдите в аккаунт, чтобы смотреть видео")
                elif self.current_user.age < 18:
                    # print(self.current_user.nickname)
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    self.log_out()
                else:
                    # print(f'whatching video"{v_nm} {v.duration}')
                    ply = ''
                    for s in range(1, v.duration + 1):
                        ply += str(s) + ' '
                        # sleep(1)
                    print(ply + 'Конец видео')


# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Вывод в консоль:
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist