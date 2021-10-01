import GeneralClassificationService
import ShoppingClassificationService
import argparse
import typing
from concurrent import futures
from pathlib import Path
from threading import Thread
import grpc
from sclog import getLogger

from grpc_helper import get_server_for_args
from plp.proto import Classification_pb2_grpc
from plp.proto import Dashboard_pb2_grpc

import WeatherClassificationService
from dotenv import load_dotenv

load_dotenv()

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
    Dashboard_pb2_grpc.add_DashboardServiceServicer_to_server(
        servicer=classification_service, server=server
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

    servers = []
    # servers.append(Thread(target=run_server,
    #                              args=(GeneralClassificationService.GeneralClassificationService(),
    #                              GeneralClassificationService.CLASSIFICATION_SERVICE_PORT,
    #                              server_args)))
    servers.append(
        Thread(
            target=run_server,
            args=(
                ShoppingClassificationService.ShoppingClassificationService(),
                ShoppingClassificationService.CLASSIFICATION_SERVICE_PORT,
                server_args,
            ),
        )
    )
    servers.append(
        Thread(
            target=run_server,
            args=(
                WeatherClassificationService.WeatherClassificationService(),
                WeatherClassificationService.CLASSIFICATION_SERVICE_PORT,
                server_args,
            ),
        )
    )
    
    # run_server(WeatherClassificationService.WeatherClassificationService(),
    #             WeatherClassificationService.CLASSIFICATION_SERVICE_PORT,  server_args)

    for server in servers:
        server.start()
    for server in servers:
        server.join()


if __name__ == "__main__":
    main()
