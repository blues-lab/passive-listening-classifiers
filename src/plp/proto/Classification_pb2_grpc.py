# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from plp.proto import Classification_pb2 as plp_dot_proto_dot_Classification__pb2


class ClassificationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ClassifyText = channel.unary_unary(
                '/plp.proto.ClassificationService/ClassifyText',
                request_serializer=plp_dot_proto_dot_Classification__pb2.ClassificationRequest.SerializeToString,
                response_deserializer=plp_dot_proto_dot_Classification__pb2.ClassificationResponse.FromString,
                )


class ClassificationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ClassifyText(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClassificationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ClassifyText': grpc.unary_unary_rpc_method_handler(
                    servicer.ClassifyText,
                    request_deserializer=plp_dot_proto_dot_Classification__pb2.ClassificationRequest.FromString,
                    response_serializer=plp_dot_proto_dot_Classification__pb2.ClassificationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'plp.proto.ClassificationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClassificationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ClassifyText(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/plp.proto.ClassificationService/ClassifyText',
            plp_dot_proto_dot_Classification__pb2.ClassificationRequest.SerializeToString,
            plp_dot_proto_dot_Classification__pb2.ClassificationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
