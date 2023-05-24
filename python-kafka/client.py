import logging

import grpc
import calendar_pb2
import calendar_pb2_grpc




def test_add_notion(stub, request):
    status = stub.RecieveData(request)
    print(status.status)
    


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:60051') as channel:
       
        stub = calendar_pb2_grpc.CalendarServiceStub(channel)
        
        print("-------------- AddNotion --------------")
        test_add_notion(stub, calendar_pb2.AddNote(id=1, note='Театр4', date_note='2023-05-23T12:27:00Z', date_remind='2023-05-23T12:49:00Z',email='trebukovD@yandex.ru'))
       
        channel.close()


if __name__ == '__main__':
    logging.basicConfig()
    run()
