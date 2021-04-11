import grpc
from sclog import getLogger

from plp.proto import Classification_pb2
from plp.proto import Classification_pb2_grpc
from shopping_classifier.shopping_skill import ShoppingSkill

logger = getLogger(__name__)

CLASSIFICATION_SERVICE_PORT = 50060


class ShoppingClassificationService(
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
            shopping_items = self.skill.find_shopping_item(request.text)
            result_extras = f"Shopping item found: {shopping_items}" 
        return Classification_pb2.ClassificationResponse(
            classifierName="Shopping",
            classification=result_classification,
            confidence=result_confidence,
            extras=result_extras,
        )
