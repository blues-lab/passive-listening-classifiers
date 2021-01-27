import grpc
from sclog import getLogger

from plp.proto import Classification_pb2
from plp.proto import Classification_pb2_grpc
from src.shopping_classifier.shopping_skill import ShoppingSkill

logger = getLogger(__name__)

CLASSIFICATION_SERVICE_PORT = 50060


class SampleClassificationService(
    Classification_pb2_grpc.ClassificationServiceServicer
):
    def __init__(self) -> None:
        super().__init__()
        self.skill = ShoppingSkill()

    def ClassifyText(self, request, context):
        logger.debug("received request %i to classify %s", request.id, request.text)
        skill_label, skill_prob = self.skill.classify(request.text)

        # Here we'd actually run the classifier
        result_classification = skill_label #"oos"
        result_confidence = skill_prob #1.0
        result_extras = "fake classification"
        if skill_label != "oos":
            result_extras = self.skill.find_shopping_item(request.text) # "fake classification"

        return Classification_pb2.ClassificationResponse(
            classifierName="sample",
            classification=result_classification,
            confidence=result_confidence,
            extras=result_extras,
        )
