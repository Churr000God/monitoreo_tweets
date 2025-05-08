# mongo_to_csv.py

from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
uri = os.getenv("MONGODB_URI")
nombre_db = "Datos_TI"
nombre_coleccion = "DatosTrend"
ruta_csv = os.path.join("data", "datos_mongo.csv")

def exportar_datos():
    try:
        print("Conectando a MongoDB...")
        client = MongoClient(uri)
        db = client[nombre_db]
        coleccion = db[nombre_coleccion]

        print("Extrayendo datos...")
        datos = list(coleccion.find())

        if not datos:
            print("No se encontraron documentos en la colección.")
            return

        df = pd.DataFrame(datos)

        if "_id" in df.columns:
            df = df.drop(columns=["_id"])

        os.makedirs(os.path.dirname(ruta_csv), exist_ok=True)
        df.to_csv(ruta_csv, index=False)
        print(f"✅ Datos exportados exitosamente a: {ruta_csv}")

    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")

if __name__ == "__main__":
    exportar_datos()
