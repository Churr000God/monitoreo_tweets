# 🐦 Monitoreo de Tweets con Análisis de Sentimiento

Este proyecto tiene como objetivo **monitorear publicaciones en Twitter** realizadas por fuentes oficiales relacionadas con seguridad y gobierno, **extraer información relevante** (alcaldía, delito, fecha, hora, menciones, hashtags), **analizar el sentimiento del mensaje**, y finalmente almacenar los datos en **MongoDB Atlas** para su posterior análisis.

---

## 📁 Estructura del Proyecto

```
monitoreo_tweets/
├── data/
│   ├── tweets.csv
│   ├── processed_tweets.csv
│   └── tweets_with_sentiment.csv
├── fetch_tweets.py
├── process_data.py
├── sentiment_analysis.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Requisitos

- Python 3.11
- Cuenta en [Twitter Developer Portal](https://developer.twitter.com/)
- Cuenta en [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)

---

## 📦 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu_usuario/monitoreo_tweets.git
cd monitoreo_tweets
```

2. Crea entorno virtual:
```bash
python3.11 -m venv venv
source venv/bin/activate
```

3. Instala dependencias:
```bash
pip install -r requirements.txt
```

4. Crea un archivo `.env` y coloca tus claves:

```env
BEARER_TOKEN=tu_token_de_twitter
MONGO_URI=tu_uri_de_mongodb
```

---

## 🚀 Ejecución

Ejecuta los scripts en este orden:

```bash
python fetch_tweets.py
python process_data.py
python sentiment_analysis.py
```

---

## 📊 Resultados

- `tweets.csv`: tweets originales
- `processed_tweets.csv`: datos enriquecidos (delito, alcaldía, etc.)
- `tweets_with_sentiment.csv`: con análisis de sentimiento
- También se insertan automáticamente en MongoDB Atlas

---

## 🧠 Herramientas utilizadas

- Python
- Tweepy (API v2)
- Pandas
- TextBlob (para sentimiento)
- MongoDB + pymongo
- dotenv

---

## 👨‍💻 Autor

Diego G.  
Estudiante de Ciencia de Datos | Tecmilenio  
Proyecto académico – Segundo semestre

---

## 📜 Licencia

Este proyecto es de uso académico. No usar datos obtenidos de la API con fines comerciales sin respetar los Términos de Uso de Twitter.