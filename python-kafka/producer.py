import json
from kafka import KafkaProducer

def func_producer(id, email_getter, note, date_remind, date_note):
    kafka_server = ['127.0.0.1:29092']

    topic = "calendar"

    producer = KafkaProducer(
        bootstrap_servers=kafka_server,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )

    data = {
        "id": id,
        "email_getter": email_getter,
        "note": note,
        "date_remind": date_remind,
        "date_note": date_note,
    }
    print('Send to kafka: ', data)
    producer.send(topic, data)
    producer.flush()


# id = 1
# email_getter = "trebukovD@yandex.ru"
# note = "Новая задача 2"
# date_remind = "2023-05-22T22:15:00Z"
# date_note = "2023-05-22T22:15:00Z"
# func_producer(id, email_getter, note, date_remind, date_note)