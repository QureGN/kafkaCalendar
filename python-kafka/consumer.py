import json
from kafka import KafkaConsumer, TopicPartition
from datetime import datetime, timedelta


def func_consumer(x):
    kafka_server = ['127.0.0.1:29092']

    topic = 'calendar'

    consumer = KafkaConsumer(
        bootstrap_servers=kafka_server,
        api_version=(0, 11, 5),
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id=None,
        consumer_timeout_ms=1000,
    )

    # consumer.subscribe(topic)
    tp = TopicPartition(topic, 0)

    consumer.assign([tp])
    consumer.seek_to_end(tp)
    lastOffset = consumer.position(tp)

    consumer.seek_to_beginning(tp)

    mes = []
    while True:
        data = next(consumer)
        msg = json.loads(data.value.decode('utf-8'))
        now_time = datetime.now()
        before_time = datetime.now() - timedelta(minutes=x)
        msg_time = datetime.fromisoformat(msg["date_remind"][:-1])

        if now_time > msg_time and msg_time > before_time:
            message = [msg["id"], msg["email_getter"], msg["note"], msg["date_remind"], msg["date_note"]]
            mes.append(message)
        # print(data)
        if data.offset == lastOffset - 1:
            break
    print('Get from kafka: ', mes)
    return mes


# print(func_consumer(100))