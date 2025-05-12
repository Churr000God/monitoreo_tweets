import pandas as pd
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
uri = os.getenv("MONGODB_URI")

# Conectar a MongoDB
client = MongoClient(uri)
db = client["ProyectoFinal"]
collection = db["TweetsClasificados"]

# Leer archivo enriquecido
csv_path = "data/tweets_with_sentiment.csv"
if not os.path.exists(csv_path):
    print(f"❌ No se encontró el archivo: {csv_path}")
    exit()

df = pd.read_csv(csv_path)
data = df.to_dict(orient="records")

if data:
    collection.insert_many(data)
    print(f"✅ Se insertaron {len(data)} documentos en la colección 'TweetsClasificados'.")
else:
    print("⚠️ No hay datos para insertar.")