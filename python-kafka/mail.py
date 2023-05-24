import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Функция для отправки сообщения на email
def send_email(email_getter, note, date_note):
    # Настройки для подключения к почтовому серверу
    email_sender = "calendar.23@mail.ru"
    # password = "kqX-6rR-JiE-c6x"                 # основной пароль от почты
    password = "SCsdxhqBBYdnatQEPzq8"  # пароль для внешнего приложения
    smtp_server = smtplib.SMTP("smtp.mail.ru", 587)
    smtp_server.starttls()

    date1 = date_note.split('T')[0]
    time1 = date_note.split('T')[1][:-1]

    # Формируем сообщение
    msg = MIMEMultipart()
    msg["Subject"] = f'Напоминание о событии: {note}'
    msg.attach(MIMEText(f'Событие: {note} \n Дата: {date1} \n Время: {time1}'))
    smtp_server.login(email_sender, password)
    smtp_server.sendmail(email_sender, email_getter, msg.as_string())


# Пример использования функции для отправки сообщения на email
# email_getter = "trebukovD@yandex.ru"  # почта получателя
# note = "Погулять с собакой"  # описание события
# date_note = "2023-05-22T22:36:00Z"  # дата события
# send_email(email_getter, note, date_note)
