# verificar_contenido.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGODB_URI")  # ✅ Coincide con tu .env
print("🧪 Usando URI:", uri)

client = MongoClient(uri)
db = client["Datos_TI"]
collection = db["DatosTrend"]

print("📦 Total de documentos:", collection.count_documents({}))
