# 🐦 Monitoreo de Tweets con Análisis de Sentimiento

Este proyecto tiene como objetivo monitorear publicaciones en Twitter relacionadas con seguridad pública, analizar su contenido (alcaldía, delito, sentimiento), y almacenar los datos en MongoDB Atlas para su posterior análisis, incluyendo la exportación a CSV y visualización en Power BI.

---

## 📁 Estructura del Proyecto

```
monitoreo_tweets/
├── data/
│   ├── tweets.csv
│   ├── processed_tweets.csv
│   ├── tweets_with_sentiment.csv
│   └── datos_mongo.csv
├── fetch_tweets.py
├── process_data.py
├── sentiment_analysis.py
├── mongo_to_csv.py
├── verificar_contenido.py
├── ejecutar_exportacion.sh
├── ejecutar_exportacion.bat
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Requisitos

- Python 3.11
- Cuenta de desarrollador en Twitter
- Cuenta en MongoDB Atlas

---

## 🛠️ Instalación

```bash
git clone https://github.com/tu_usuario/monitoreo_tweets.git
cd monitoreo_tweets
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🔐 Variables de entorno

Crea un archivo `.env` basado en el siguiente formato:

```env
BEARER_TOKEN=tu_token_de_twitter
MONGODB_URI=mongodb+srv://usuario:contraseña@tuserver.mongodb.net/?retryWrites=true&w=majority
```

---

## 🚀 Ejecución

```bash
python fetch_tweets.py
python process_data.py
python sentiment_analysis.py
python mongo_to_csv.py
```

---

## 🖥️ Automatización

- **Linux**: ejecuta `./ejecutar_exportacion.sh`
- **Windows**: doble clic en `ejecutar_exportacion.bat`

---

## 📊 Visualización en Power BI

1. Abrir Power BI Desktop
2. "Obtener datos" → Texto/CSV
3. Selecciona `data/datos_mongo.csv`
4. Clic en "Cargar" y comienza a graficar

⚠️ *Nota: Power BI Desktop solo está disponible para Windows.*

---

## 📜 Licencia

Proyecto académico del Tecmilenio – Ciencia de Datos – Segundo semestre.