import grpc
from sclog import getLogger

from plp.proto import Classification_pb2
from plp.proto import Classification_pb2_grpc
from plp.proto import Dashboard_pb2_grpc
from plp.proto import Dashboard_pb2

from shopping_classifier.shopping_skill import ShoppingSkill

logger = getLogger(__name__)

CLASSIFICATION_SERVICE_PORT = 50060


class ShoppingClassificationService(
    Classification_pb2_grpc.ClassificationServiceServicer,
    Dashboard_pb2_grpc.DashboardServiceServicer
):
    def __init__(self) -> None:
        super().__init__()
        self.skill = ShoppingSkill()
        self.previous_classifications = []

    def getDashboardData(self, request: Dashboard_pb2.DashboardRequest, context):
        num_to_classify = max(request.classificationLimit, 1)

        return Dashboard_pb2.DashboardResponse(
            text=self.previous_classifications[:num_to_classify],
            classificationName="shopping"
        )


    def ClassifyText(self, request, context):
        logger.debug("received request %i to classify %s", request.id, request.text)
        skill_label, skill_prob = self.skill.classify(request.text)

        # Here we'd actually run the classifier
        result_classification = skill_label #"oos"
        result_confidence = skill_prob #1.0
        result_extras = "fake classification"
        if skill_label != "oos":
            _, prob, shopping_item = self.skill.find_shopping_item(request.text)
            result_extras = f"Shopping item found: {shopping_item} with prob {prob}" 
        
        self.previous_classifications.append(f"{result_classification}; {result_confidence}")
        return Classification_pb2.ClassificationResponse(
            classifierName="sample",
            classification=result_classification,
            confidence=result_confidence,
            extras=result_extras,
        )
