# Задача "Рассылка писем"
# 1. Создайте функцию send_email, которая принимает 2 обычных аргумента:
# message(сообщение), recipient(получатель) и 1 обязательно именованный аргумент
# со значением по умолчанию sender = "university.help@gmail.com".
def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    # 2. Если строки recipient и sender не содержит "@"
    # или не оканчивается на ".com"/".ru"/".net", то вывести на экран(в консоль)
    # строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
    if '@' not in recipient or '@' not in sender \
    or ((sender[-3::] not in ['.ru']
         and sender[-4::] not in ['.com']
         and sender[-4::] not in ['.net'])
    or (recipient[-3::] not in ['.ru']
         and recipient[-4::] not in ['.com']
         and recipient[-4::] not in ['.net'])):
        print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')

    # 3. Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
    elif str(recipient) == str(sender):
        print("Нельзя отправить письмо самому себе!")

    # 4. Если же отправитель по умолчанию - university.help@gmail.com,
    # то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>.')
    # 5. В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>.')



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')