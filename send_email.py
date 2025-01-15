def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if "@" not in recipient and sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    suffixes = ('.com', '.ru', '.net')
    if not recipient.endswith(suffixes) or not sender.endswith(suffixes):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса <{sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
