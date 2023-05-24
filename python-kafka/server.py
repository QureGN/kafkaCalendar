from concurrent import futures
import logging

import grpc
import calendar_pb2
import calendar_pb2_grpc

from gRPCError import error_pb2, error_pb2_grpc

from consumer import func_consumer
from producer import func_producer
from mail import send_email
from time import sleep

SLEEP_TIME = 1  # период обновления информации (в минутах)


class CalendarServicer(calendar_pb2_grpc.CalendarServiceServicer):

    def RecieveData(self, request, context):
        print('New request: Add notion')
        print('note:', request.note)
        print('date_note', request.date_note)
        print('email', request.email)

        # проверим, что данные приходят не пустые
        if not (not request.id) and not (not request.email) and not (not request.note) and not (
        not request.date_remind) and not (not request.date_note):
            func_producer(request.id, request.email, request.note, request.date_remind, request.date_note)
            status = calendar_pb2.Status(status=True)
        else:
            status = calendar_pb2.Status(status=False)

        return status


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calendar_pb2_grpc.add_CalendarServiceServicer_to_server(
        CalendarServicer(), server)
    server.add_insecure_port('[::]:60051')
    server.add_insecure_port('0.0.0.0:30000')
    server.start()
    print('gRPC Server started successfully')

    # server.wait_for_termination()
    try:
        while True:
            consumer_msgs = func_consumer(SLEEP_TIME)
            while True:
                if consumer_msgs != []:
                    for msg in consumer_msgs:
                        try:
                            print('Send message for email:', msg[1])
                            send_email(msg[1], msg[2], msg[4])
                        except Exception as e:
                            print('Can not send imail')
                            channel = grpc.insecure_channel('localhost:50051')
                            stub = error_pb2_grpc.ErrorMethodStub(channel)
                            print('----- SendError -----')
                            response = stub.SendErrot(error_pb2.AddError(id=msg[0], flag=False))
                            print(response, end='')
                    consumer_msgs = []
                else:
                    break
            sleep(SLEEP_TIME * 60)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
