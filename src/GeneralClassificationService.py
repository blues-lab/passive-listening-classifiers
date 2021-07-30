import grpc
from sclog import getLogger

from plp.proto import Classification_pb2
from plp.proto import Classification_pb2_grpc
from general_classifier.general_classifier import GeneralClassifierSkill
from plp.proto import PermissionPoll_pb2, PermissionDisplay_pb2_grpc

logger = getLogger(__name__)

CLASSIFICATION_SERVICE_PORT = 50061


class GeneralClassificationService(
    Classification_pb2_grpc.ClassificationServiceServicer
):
    def __init__(self) -> None:
        super().__init__()
        self.skill = GeneralClassifierSkill()

    # def ClassifyText(self, request, context):
    #     logger.debug("received general classification request %i to classify %s", request.id, request.text)
    #     skill_label, skill_prob = self.skill.classify(request.text)

    #     # Here we'd actually run the classifier
    #     result_classification = skill_label #"oos"
    #     result_confidence = skill_prob #1.0
    #     result_extras = ""
    #     return Classification_pb2.ClassificationResponse(
    #         classifierName="sample",
    #         classification=result_classification,
    #         confidence=result_confidence,
    #         extras=result_extras,
    #     )

    def ClassifyText(self, request, context):
            logger.debug("received general classification request %i to classify %s", request.id, request.text)
            skill_label, skill_prob = self.skill.classify(request.text)

            # Here we'd actually run the classifier
            result_classification = skill_label #"oos"
            
            return PermissionPoll_pb2.PermissionPollResponse(
                template="Would like to look up this info: ",
                slot=result_classification,
                url="example.com"
            )