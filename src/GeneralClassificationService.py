import grpc
from sclog import getLogger

from plp.proto import Classification_pb2
from plp.proto import Classification_pb2_grpc
from general_classifier.general_classifier import GeneralClassifierSkill
from plp.proto import Dashboard_pb2_grpc
from plp.proto import Dashboard_pb2

logger = getLogger(__name__)

CLASSIFICATION_SERVICE_PORT = 50060


class GeneralClassificationService(
    Classification_pb2_grpc.ClassificationServiceServicer,
    Dashboard_pb2_grpc.DashboardServiceServicer,
):
    def __init__(self) -> None:
        super().__init__()
        self.skill = GeneralClassifierSkill()
        self.previous_classifications = []

    def getDashboardData(self, request: Dashboard_pb2.DashboardRequest, context):
        num_to_classify = max(request.classificationLimit, 1)

        return Dashboard_pb2.DashboardResponse(
            text=self.previous_classifications[:num_to_classify],
            classificationName="general",
        )

    def ClassifyText(self, request, context):
        logger.debug(
            "received genera classification request %i to classify %s",
            request.id,
            request.text,
        )
        skill_label, skill_prob = self.skill.classify(request.text)

        # Here we'd actually run the classifier
        result_classification = skill_label  # "oos"
        result_confidence = skill_prob  # 1.0
        result_extras = ""
        return Classification_pb2.ClassificationResponse(
            classifierName="sample",
            classification=result_classification,
            confidence=result_confidence,
            extras=result_extras,
        )
