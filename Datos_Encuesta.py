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
collection = db["Encuesta"]

# Leer archivo Excel
excel_path = "data/DatosEncuesta.xlsx"
if not os.path.exists(excel_path):
    print(f"❌ No se encontró el archivo: {excel_path}")
    exit()

df = pd.read_excel(excel_path, engine='openpyxl')
data = df.to_dict(orient="records")

if data:
    collection.insert_many(data)
    print(f"✅ Se insertaron {len(data)} documentos en la colección 'Encuesta'.")
else:
    print("⚠️ No hay datos para insertar.")