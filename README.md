# 🌦️ Intelligent Hybrid Weather Agent (Rasa + Streamlit)

Este proyecto implementa un **agente inteligente híbrido** que combina:

- Rasa (NLU + diálogo)
- Base de conocimiento experta
- Reglas de razonamiento
- Cálculo de probabilidad de lluvia basado en factores ambientales
- Umbral adaptable mediante sensibilidad
- Interfaz gráfica con Streamlit

El agente puede:
- Estimar probabilidad de lluvia usando humedad, presión y variación de temperatura.  
- Explicar por qué existe riesgo de lluvia.  
- Consultar el estado del clima actual.  
- Ajustar dinámicamente la sensibilidad de los alertas.  
- Funcionar en consola o en una interfaz gráfica web.

---
# ⚙️ 1. Instalación y Configuración del Entorno

A continuación se muestran los comandos necesarios para instalar todo lo que el agente utiliza.

### 🔧 Paso 1 — Crear entorno virtual (Conda)

```bash
conda create -n weather_agent python=3.10
conda activate weather_agent
```

# 🔧 Paso 2 — Instalar Rasa
```bash
pip install rasa
```

# Paso 3 — Instalar Streamlit (interfaz gráfica)
```bash
pip install streamlit
```

# Paso 4 — Instalar dependencias adicionales
```bash
pip install requests
```

# 🤖 2. Entrenar el Modelo de Rasa
Desde la carpeta del proyecto:
```bash
rasa train
```
# 🚀 3. Levantar el Agente (Servicios Backend)
## ▶ Levantar servidor de acciones (obligatorio)
```bash
rasa run actions
```
Mantén esta ventana abierta.

## ▶ Levantar servidor Rasa (API REST)
```bash
rasa run -m models --enable-api --cors "*"
```
# 🖥️ 4. Ejecutar la Interfaz Gráfica (Streamlit)
```bash
streamlit run weather_chat.py
```

Esto abrirá la interfaz en:
http://localhost:8501

# 💬 5. Consultas Disponibles para el Usuario
Aquí se muestran todas las consultas posibles que el agente entiende.
## 🌧️ Consultas sobre Probabilidad de Lluvia
Estas preguntas activan el cálculo inteligente basado en humedad, presión y temperatura.

“What is the chance of rain?”

“Will it rain today?”

“Is there a rain risk right now?”

“Could you estimate the rain probability?”

“Should I take my clothes inside?”

## 🌤️ Consultas sobre Clima Actual
“What is the current weather?”

“Tell me the weather conditions.”

“How is the weather outside?”

“What is the temperature and humidity?”

## 🧠 Consultas de Explicación del Riesgo
“Why is the rain risk high?”

“Explain the alert.”

“What factors increased the risk?”

“Why did you warn me?”

## ⚙️ Consultas de Ajuste de Sensibilidad
Permiten modificar umbrales dinámicamente.

“Set alert sensitivity to high.”

“Lower the alert threshold.”

“Increase alert sensitivity.”

“Reduce false alarms.”

## 🤖 Consultas Adicionales Compatibles
“Do I need to worry about rain?”

“Is it a good day to dry clothes?”

“Is rain expected soon?”

“Is the weather stable?”

