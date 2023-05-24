from producer import func_producer
from consumer import func_consumer
from mail import send_email
from time import sleep
import datetime
from server import serve
import logging

SLEEP_TIME = 10    # период обновления информации (в минутах)

producer_msgs = []    # массив для отправки сообщений в брокер
consumer_msgs = []    # массив для получения сообщений из брокера

while True:
    # if email_sender != '':
    #     func_producer(id, email_sender, note, date_remind, date_note)

    consumer_msgs = func_consumer(SLEEP_TIME)
    while True:
        if consumer_msgs != []:
            for msg in consumer_msgs:
                try:
                    print('send email')
                    send_email(msg[1], msg[2], msg[4])
                    consumer_msgs = []
                except Exception as e:
                    print('Can not send imail')
                    consumer_msgs = []
        else:
            break

    sleep(SLEEP_TIME*60)
