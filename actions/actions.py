from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .knowledge_base import knowledge_base
import random

class ActionCalculateRainRisk(Action):
    def name(self):
        return "action_calculate_rain_risk"

    def run(self, dispatcher, tracker, domain):

        humidity = random.randint(40, 100)
        pressure = random.randint(995, 1020)
        temperature_drop = random.choice([True, False])
        api_forecast = random.choice(["clear", "rain"])

        thresholds = knowledge_base["thresholds"]
        rain_risk = 0.0
        reasons = []

        if humidity > thresholds["humidity_high"]:
            rain_risk += 0.4
            reasons.append("High humidity detected")

        if pressure < thresholds["pressure_low"]:
            rain_risk += 0.3
            reasons.append("Low atmospheric pressure")

        if temperature_drop:
            rain_risk += 0.3
            reasons.append("Sudden temperature drop")

        if api_forecast == "rain":
            rain_risk += 0.5
            reasons.append("External API forecast predicts rain")

        if rain_risk > 1: rain_risk = 1
        
        risk_percentage = round(rain_risk * 100, 2)

        dispatcher.utter_message(
            text=f"Estimated rain probability: {risk_percentage}%.\nReasons: {', '.join(reasons)}."
        )

        return []


class ActionGetCurrentWeather(Action):
    def name(self):
        return "action_get_current_weather"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="The current weather data has been retrieved.")
        return []


class ActionExplainRisk(Action):
    def name(self):
        return "action_explain_risk"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="The system uses humidity, pressure, temperature variation and API forecasts to determine rain risk.")
        return []


class ActionChangeSensitivity(Action):
    def name(self):
        return "action_change_sensitivity"

    def run(self, dispatcher, tracker, domain):
        level = tracker.latest_message.get("entities")
        dispatcher.utter_message(text=f"Alert sensitivity updated.")
        return []
