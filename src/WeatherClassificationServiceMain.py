import argparse
from threading import Thread
from sclog import getLogger

from grpc_helper import get_server_for_args
from plp.proto import Classification_pb2_grpc
import WeatherClassificationService


logger = getLogger(__name__)


def run_server(classification_service, port, args):
    server = get_server_for_args(
        port,
        args.key,
        args.cert,
        args.root,
    )

    # Can also be seperate on to a seperate server
    Classification_pb2_grpc.add_ClassificationServiceServicer_to_server(
        servicer=classification_service,
        server=server,
    )
    server.start()
    server.wait_for_termination()


def main():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument(
        "--key",
        type=str,
        help="Path to private key",
    )
    parser.add_argument(
        "--cert",
        type=str,
        help="Path to certificate",
    )
    parser.add_argument(
        "--root",
        type=str,
        help="Path to root certificates",
    )
    server_args = parser.parse_args()

    run_server(
        WeatherClassificationService.WeatherClassificationService(),
        WeatherClassificationService.CLASSIFICATION_SERVICE_PORT,
        server_args,
    )


if __name__ == "__main__":
    main()
