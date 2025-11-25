from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

# =============================================================
# === VARIABLES ESTÁTICAS PARA SIMULACIÓN (Módulos Híbridos) ===
# =============================================================

# Simula el umbral óptimo ajustado por el Algoritmo Genético (GA)
UMBRAL_HUMEDAD_GA_SIMULADO = 75.0 

# Simula los datos climáticos actuales (pre-procesados por AIS)
DATOS_CLIMA_SIMULADOS = {
    "humedad": 82,   # Valor de humedad actual
    "prob_lluvia": 55 # Probabilidad de lluvia actual (en %)
}

# Historial simulado para la consulta
HISTORIAL_SIMULADO = [
    {"fecha": "2025-11-20 10:00", "alerta": "ALERTA - Lluvia Fuerte", "humedad": 88},
    {"fecha": "2025-11-19 15:30", "alerta": "Sin Riesgo", "humedad": 65},
    {"fecha": "2025-11-18 08:45", "alerta": "ALERTA - Humedad Alta", "humedad": 80},
]

# =============================================================
# === ACCIONES PERSONALIZADAS ===
# =============================================================

class ActionCheckWeatherRisk(Action):
    """
    Simula la ejecución del Módulo de Percepción y Razonamiento Híbrido.
    Usa valores estáticos para probar la lógica de la regla.
    """
    def name(self) -> Text:
        return "action_check_weather_risk"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # 1. Obtener Umbral óptimo (GA Simulado)
        ga_umbral = UMBRAL_HUMEDAD_GA_SIMULADO
        
        # 2. Obtener Datos Climáticos (AIS Simulado)
        humedad = DATOS_CLIMA_SIMULADOS["humedad"]
        prob_lluvia = DATOS_CLIMA_SIMULADOS["prob_lluvia"]
            
        # 3. Módulo de Razonamiento Lógico (Regla SIMULADA)
        # Regla: Si la humedad > umbral GA Y la probabilidad de lluvia es alta (> 40%)
        if humedad > ga_umbral and prob_lluvia > 40:
            # Si se activa la regla, emitir la alerta (usando el response del domain)
            estado_clima = f"ALERTA ACTIVADA. Humedad: {humedad}%. Lluvia: {prob_lluvia}%."
            dispatcher.utter_message(response="utter_alerta_riesgo", umbral_actual=ga_umbral)
        else:
            # Si no hay riesgo, mostrar el estado normal
            estado_clima = f"Riesgo bajo. Humedad: {humedad}%. Lluvia: {prob_lluvia}%."
            dispatcher.utter_message(response="utter_clima_actual", 
                                     estado_clima_actual=estado_clima, 
                                     umbral_actual=ga_umbral)

        return [
            SlotSet("estado_clima_actual", estado_clima),
            SlotSet("umbral_actual", ga_umbral)
        ]

class ActionUpdateSensitivity(Action):
    """
    Simula la actualización de umbrales. Solo valida el flujo de la conversación.
    """
    def name(self) -> Text:
        return "action_update_sensitivity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        clima_variable = tracker.get_slot('clima_variable') if tracker.get_slot('clima_variable') else "humedad"
        sensibilidad_nivel = tracker.get_slot('sensibilidad_nivel') if tracker.get_slot('sensibilidad_nivel') else "ajustado"
        
        # En una implementación real, aquí se enviarían los datos al GA.
        # Por ahora, solo confirmamos la acción al usuario.
        
        dispatcher.utter_message(response="utter_confirmacion_ajuste", 
                                 clima_variable=clima_variable, 
                                 sensibilidad_nivel=sensibilidad_nivel)

        # Limpiamos los slots después de usarlos
        return [
            SlotSet("clima_variable", None),
            SlotSet("sensibilidad_nivel", None)
        ]

class ActionProcessFeedback(Action):
    """
    Simula el envío de la retroalimentación al Módulo de Gestión y Aprendizaje.
    """
    def name(self) -> Text:
        return "action_process_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # 1. Obtener entidades de feedback
        feedback_entities = tracker.latest_message.get('entities', [])
        tipo_feedback = next((e['value'] for e in feedback_entities if e['entity'] == 'tipo_feedback'), 'desconocido')
        
        # 2. Simulación de registro
        # En una implementación real, aquí se registraría el evento y el tipo_feedback
        print(f"--- SIMULACIÓN DE REGISTRO --- Feedback recibido: {tipo_feedback}. Se usa para reentrenar el GA.")
        
        dispatcher.utter_message(response="utter_agradecimiento_feedback")

        return []

class ActionRetrieveHistory(Action):
    """
    Muestra un historial simulado del Registro Histórico.
    """
    def name(self) -> Text:
        return "action_retrieve_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Formatear los registros simulados
        resumen = "\n".join([
            f"- {r['fecha']}: {r['alerta']} (Humedad: {r['humedad']}%)" for r in HISTORIAL_SIMULADO
        ])
        
        dispatcher.utter_message(f"Resumen de las últimas alertas:\n{resumen}")
        
        return []