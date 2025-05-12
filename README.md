
# 🐦 Sistema Inteligente de Monitoreo de Tweets y Encuestas

Este sistema automatiza la recopilación, análisis y visualización de datos provenientes de Twitter (X) y de encuestas locales. Los datos se enriquecen, clasifican, almacenan en MongoDB Atlas y luego se visualizan mediante Power BI.

---

## 📁 Estructura del Proyecto

```
MONITOREO_TWEETS/
├── data/
│   ├── datos_mongo.csv
│   ├── DatosEncuesta.xlsx
│   ├── tweets.csv
│   └── tweets_with_sentiment.csv
├── .env
├── .env.example
├── README.md
├── requirements.txt
├── ejecutar_exportacion.bat
├── ejecutar_exportacion.sh
├── fetch_tweets.py
├── main.py
├── Datos_Encuesta.py
├── mongo_to_csv.py
├── upload_to_mongo.py
```

---

## ⚙️ Requisitos

- Python 3.11
- Cuenta en [Twitter Developer](https://developer.twitter.com/)
- MongoDB Atlas con URI válido
- Power BI Desktop
- Librerías Python (instalables con `pip install -r requirements.txt`)

---

## 🚀 Flujo del Sistema Inteligente

El sistema ejecuta los siguientes pasos automatizados:

1. **`main.py`**  
   Descarga tweets desde la API de Twitter, analiza el sentimiento y clasifica por alcaldía y tipo de servicio.  
   ✔ Guarda los datos en `data/tweets_with_sentiment.csv`.

2. **`upload_to_mongo.py`**  
   Carga los tweets clasificados a MongoDB Atlas (colección `TweetsClasificados`).

3. **`mongo_to_csv.py`**  
   Exporta los documentos desde MongoDB a `data/datos_mongo.csv` para uso en Power BI.

4. **`Datos_Encuesta.py`**  
   Inserta respuestas de encuesta desde `DatosEncuesta.xlsx` en la colección `Encuesta`.

---

## 🧪 Ejecución Manual

### En Linux

```bash
chmod +x ejecutar_exportacion.sh
./ejecutar_exportacion.sh
```

### En Windows

Doble clic sobre `ejecutar_exportacion.bat`.

---

## 🔐 Archivo de entorno `.env`

Debe contener tus claves de API:

```env
BEARER_TOKEN=tu_token_de_twitter
MONGODB_URI=tu_uri_de_mongo
```

---

## 📊 Visualización en Power BI

1. Abre **Power BI Desktop**
2. Conecta los archivos:
   - `data/datos_mongo.csv`
   - `data/DatosEncuesta.xlsx`
3. Crea al menos 6 visualizaciones:
   - 3 con datos de tweets (alcaldía, sentimiento, servicio)
   - 3 con datos de encuesta (edad, percepción, satisfacción, etc.)
4. Opcional: Crea botones para navegar entre secciones (Twitter y Encuesta)

---

## 📸 Evidencias de funcionamiento

- Ejecución en terminal (pantalla negra)
- Visualización de documentos en MongoDB
- Exportación a CSV desde MongoDB
- Datos cargados en Power BI
- Gráficas completas por cada fuente

---

## 🛡 Recomendaciones

- Evita duplicar tweets: el sistema verifica si ya existe `tweets_with_sentiment.csv`
- Usa `TextBlob` para análisis de sentimiento
- Aplica pausas (`time.sleep()`) para evitar el rate limit de la API

---

**Autor:** Diego Hermilo Guillén  
**Fecha límite del proyecto:** 11 de mayo  
**Curso:** Ciencia de Datos / Proyecto Final
