import collections
from weather_classifier.classify_weather_trigger import is_trigger_sentence_transformer
from weather_classifier.location_recognition.pipeline import compute_loc

class WeatherClassifierSkill(object):
    def __init__(self):
        self.log = collections.deque(maxlen=100)

    def classify(self, text):
        self.log.extend(text)
        if not is_trigger_sentence_transformer(text):
            return "No Trigger", 1.0
        location = compute_loc(list(self.log))
        label = "{} identified for weather app".format(location)
        prob = 1.0
        return label, prob
