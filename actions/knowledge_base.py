# knowledge_base.py

knowledge_base = {
    "thresholds": {
        "humidity_high": 70,       # % humidity
        "pressure_low": 1005,      # hPa
        "temperature_drop": 3,     # sudden drop in °C
    },

    "expert_rules": [
        "IF humidity > humidity_high THEN rain_risk += 0.4",
        "IF pressure < pressure_low THEN rain_risk += 0.3",
        "IF sudden_temperature_drop == True THEN rain_risk += 0.3",
        "IF api_forecast == 'rain' THEN rain_risk += 0.5"
    ],

    "anomaly_patterns": [
        "sudden_humidity_spike",
        "pressure_anomaly",
        "unexpected_temperature_variation"
    ]
}
