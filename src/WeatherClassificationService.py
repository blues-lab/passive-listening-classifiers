import grpc
from sclog import getLogger

from plp.proto import Classification_pb2
from plp.proto import Classification_pb2_grpc
from weather_classifier.weather_classifier import WeatherClassifierSkill
from plp.proto import Dashboard_pb2_grpc
from plp.proto import Dashboard_pb2
import os
import requests
import datetime

logger = getLogger(__name__)

CLASSIFICATION_SERVICE_PORT = 50060


class WeatherClassificationService(
    Classification_pb2_grpc.ClassificationServiceServicer,
    Dashboard_pb2_grpc.DashboardServiceServicer
):
    def __init__(self) -> None:
        super().__init__()
        self.skill = WeatherClassifierSkill()
        self.previous_location = []
        self.cached_weather_results = {}

    def getDashboardData(self, request, context):
        logger.debug("received weather dashboard request")
        # num_to_classify = max(request.classificationLimit, 1)
        if not self.previous_location:
            return Dashboard_pb2.DashboardResponse(
                status=405,
                text=["weather locations need to be mentioned"]
            )
        
        location = self.previous_location[-1]
        logger.debug("Previous location %s", location)
        current_time = datetime.datetime.now()
        if location in self.cached_weather_results and self.cached_weather_results[location]["expiry"] < current_time:
            return self.cached_weather_results[location]["result"]
        
        api_key = os.getenv("WEATHER_API_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
        results = requests.get(url).json()
        logger.debug("making request with url %s", url)

        weather = results["weather"][0]["description"]
        temp = results["main"]["temp"]
        kelvin_temp = float(temp)
        celcisus_temp = kelvin_temp - 273.15
        fahrenheit_temp = celcisus_temp * ( 9 / 5 ) + 32
        temp = fahrenheit_temp

        logger.debug(f"Weather in {location} is {weather} at {temp}")

        response = Dashboard_pb2.DashboardResponse(
            text=[f"Weather in {location} is {weather} at {temp}"],
            classificationName="weather",
            status=200
        )
        
        self.cached_weather_results[location] = {
            "expiry": datetime.datetime.now() + datetime.timedelta(hours=1),
            "result": response,
        }        

        return response

    def ClassifyText(self, request, context):
        logger.debug("received weather classification request %i to classify %s", request.id, request.text)
        skill_label, skill_prob = self.skill.classify(request.text)

        # Here we'd actually run the classifier
        result_classification = skill_label #"oos"
        result_confidence = skill_prob #1.0
        result_extras = ""
        self.previous_location.append(result_classification)
        logger.debug("Resulting Classification %s %s", request.text, result_classification)
        return Classification_pb2.ClassificationResponse(
            classifierName="weather",
            classification=result_classification,
            confidence=result_confidence,
            extras=result_extras,
        )
