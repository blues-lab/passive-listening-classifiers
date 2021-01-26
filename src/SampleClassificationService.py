import grpc
from sclog import getLogger

from plp.proto import Classification_pb2
from plp.proto import Classification_pb2_grpc

logger = getLogger(__name__)

CLASSIFICATION_SERVICE_PORT = 50060


class SampleClassificationService(
    Classification_pb2_grpc.ClassificationServiceServicer
):
    def ClassifyText(self, request, context):
        logger.debug("received request %i to classify %s", request.id, request.text)

        # Here we'd actually run the classifier
        result_classification = "oos"
        result_confidence = 1.0
        result_extras = "fake classification"

        return Classification_pb2.ClassificationResponse(
            classifierName="sample",
            classification=result_classification,
            confidence=result_confidence,
            extras=result_extras,
        )
