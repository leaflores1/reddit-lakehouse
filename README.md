# 🌎 Reddit Lakehouse: Real-Time Data Pipeline

Este proyecto implementa una arquitectura moderna de captura y almacenamiento de datos en tiempo real desde Reddit utilizando AWS Kinesis y S3. Los datos se recolectan desde un subreddit específico y se almacenan para futuras transformaciones y análisis.

## 🚀 Objetivo

Capturar publicaciones de Reddit en tiempo real, enviarlas a un stream de Amazon Kinesis y luego persistirlas automáticamente en un bucket de S3 usando Amazon Firehose. Este pipeline es escalable y sirve como base para análisis, dashboards y productos de datos.

---

## 📦 Estructura del Proyecto

reddit-lakehouse/
├── src/
│ └── producer/
│ ├── reddit_producer.py # Script principal: captura y envía a Kinesis
│ ├── config.ini # Credenciales y configuración de Reddit
│ └── test_login.py # Script de prueba de login con PRAW
├── README.md

---

## ⚙️ Requisitos

- Cuenta en AWS con permisos sobre Kinesis y S3
- Perfil configurado en AWS CLI (`reddit-dev`)
- Reddit app configurada en [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
- Python 3.10+  
- Bibliotecas instaladas:
  pip install boto3 praw

🧾 Configuración
1. config.ini con credenciales de Reddit
[reddit]
client_id = TU_CLIENT_ID
client_secret = TU_SECRET
username = TU_USUARIO
password = TU_PASSWORD
user_agent = script:stream-leandro:v1.0 (by u/TU_USUARIO)

2. Credenciales de AWS
Asegurate de tener un perfil en tu PC con permisos para Kinesis:

aws configure --profile reddit-dev

🧠 ¿Cómo funciona?
El script reddit_producer.py se conecta a Reddit con PRAW.

Se suscribe al stream de nuevos posts de un subreddit (worldnews, argentina, etc).

Por cada post:

Lo convierte en JSON

Lo envía al stream de Kinesis reddit-stream

Firehose (previamente configurado) toma los datos y los guarda en S3.

▶️ Ejecución
python src/producer/reddit_producer.py
Verás:
Iniciando stream y envío a Kinesis...
Enviando: World leaders react to...
Enviando a Kinesis...
📊 Visualización
Ir a AWS Console → Kinesis → reddit-stream → Monitoreo.

Ver si aumentan métricas como:

PutRecord.Success

IncomingBytes

Luego, ver en el bucket de S3 los archivos JSON con los datos persistidos.