# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from gRPCError import error_pb2 as gRPCError_dot_error__pb2


class ErrorMethodStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendErrot = channel.unary_unary(
                '/error_proto.ErrorMethod/SendErrot',
                request_serializer=gRPCError_dot_error__pb2.AddError.SerializeToString,
                response_deserializer=gRPCError_dot_error__pb2.Status.FromString,
                )


class ErrorMethodServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendErrot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ErrorMethodServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendErrot': grpc.unary_unary_rpc_method_handler(
                    servicer.SendErrot,
                    request_deserializer=gRPCError_dot_error__pb2.AddError.FromString,
                    response_serializer=gRPCError_dot_error__pb2.Status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'error_proto.ErrorMethod', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ErrorMethod(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendErrot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/error_proto.ErrorMethod/SendErrot',
            gRPCError_dot_error__pb2.AddError.SerializeToString,
            gRPCError_dot_error__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
