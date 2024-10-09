# Домашняя работа по уроку "Способы вызова функции"

def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    list_domen = '.com', '.ru', '.net' # кортедж - занимает меньше памяти
    #print(list_domen)

    # Проверим присутствует ли разделитель имени адреса и домена почтового сервера
    if '@' not in recipient or '@' not in sender:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    else:
        # Проверим содержание допустимых доменов первого уровня
        recipient_domen = False
        sender_domen = False
        for i in range(len(list_domen)):
            aaa = list_domen[i]
            #print(aaa)
            # Проверяем получателя
            bbb = recipient[-len(aaa):]
            #print(bbb)
            if aaa in bbb: #and aaa not in sender:
                recipient_domen = True
            # Проверяем отправителя
            bbb = sender[-len(aaa):]
            # print(bbb)
            if aaa in bbb:
                sender_domen = True
            #print(recipient[-3:])
        if not (recipient_domen and sender_domen):
            return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    # Проверим на совпадение имен отправителя и получателя
    if recipient == sender:
        return print(f'Нельзя отправить письмо самому себе!')
    # Проверим отправителя
    if sender == "university.help@gmail.com":
        return print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        return print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


#send_email('Привет.', 'maruschak.oa@yandex.ru')
#send_email('Привет.', 'maruschak.oa@yandex.ru', sender='maruschak.oa@yandex.ru') print(f ‘{i} x {j} = {i} * {j}’)»
#send_email('Привет.', 'maruschak.oa@yandex.ru', sender='help@yandex.ru')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')