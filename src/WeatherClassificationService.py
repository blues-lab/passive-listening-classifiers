import grpc
from sclog import getLogger

from plp.proto import Classification_pb2
from plp.proto import Classification_pb2_grpc
from weather_classifier.weather_classifier import WeatherClassifierSkill

logger = getLogger(__name__)

CLASSIFICATION_SERVICE_PORT = 50060


class WeatherClassificationService(
    Classification_pb2_grpc.ClassificationServiceServicer
):
    def __init__(self) -> None:
        super().__init__()
        self.skill = WeatherClassifierSkill()

    def ClassifyText(self, request, context):
        logger.debug("received weather classification request %i to classify %s", request.id, request.text)
        skill_label, skill_prob = self.skill.classify(request.text)

        # Here we'd actually run the classifier
        result_classification = skill_label #"oos"
        result_confidence = skill_prob #1.0
        result_extras = ""
        return Classification_pb2.ClassificationResponse(
            classifierName="weather",
            classification=result_classification,
            confidence=result_confidence,
            extras=result_extras,
        )
