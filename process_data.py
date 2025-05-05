import pandas as pd 
import re
import os
from pymongo import MongoClient
from dotenv import load_dotenv

#Cargar variables de entorno desde .env
load_dotenv()
MONGO_URI = os.getenv('MONGODB_URI')

#Cargar Datos
df = pd.read_csv('data/tweets.csv')

#Listas de busqueda
alcaldias = [
    "Álvaro Obregón", "Azcapotzalco", "Benito Juárez", "Coyoacán",
    "Cuajimalpa de Morelos", "Cuauhtémoc", "Gustavo A. Madero",
    "Iztacalco", "Iztapalapa", "La Magdalena Contreras", "Miguel Hidalgo",
    "Milpa Alta", "Tláhuac", "Tlalpan", "Venustiano Carranza", "Xochimilco"
]

delitos = {
    "Asalto": r"\bAsalto\b",
    "Asesinato": r"\bAsesinato\b",
    "Secuestro": r"\bSecuestro\b"
}

hora_regex = r"\b\d{1,2}:\d{2}\b"
fecha_regex = r"\b\d{1,2}/\d{1,2}/\d{2,4}\b"

#Funcion de extraccion
def extraer_alcaldia(texto):
    return next((a for a in alcaldias if a in texto), None)

def extraer_delito(texto):
    return next((delito for delito, pattern in delitos.items() if re.search(pattern, texto, re.IGNORECASE)), None)

def extraer_hora(texto):
    match = re.search(hora_regex, texto)
    return match.group(0) if match else None

def extraer_fecha(texto):
    match = re.search(fecha_regex, texto)
    return match.group(0) if match else None

def extraer_menciones(texto):
    return re.findall(r"@[\w_]+", texto)

def extraer_hashtags(texto):
    return re.findall(r"#\w+", texto)

#Procesar Dataframe
def procesar_dataframe(df):
    df['Alcaldía'] = df['Text'].apply(extraer_alcaldia)
    df['Delito'] = df['Text'].apply(extraer_delito)
    df['Fecha'] = df['Text'].apply(extraer_fecha)
    df['Hora'] = df['Text'].apply(extraer_hora)
    df['Autor'] = df['Author_ID']
    df['Menciones'] = df['Text'].apply(extraer_menciones)
    df['Hashtags'] = df['Text'].apply(extraer_hashtags)
    return df[['Autor', 'Alcaldía', 'Delito', 'Fecha', 'Hora', 'Menciones', 'Hashtags', 'Text']]

#Aplicar procesamiento
processed_df = procesar_dataframe(df)

#Guardar localmente
os.makedirs('data', exist_ok=True)
processed_df.to_csv('data/processed_tweets.csv', index=False)
print("✅ Datos procesados guardados en 'data/processed_tweets.csv'")

#Subir a MongoDB
try:
    client = MongoClient(MONGO_URI)
    db = client["Datos_TI"]
    collection = db["DatosTrend"]

    data_dict = processed_df.to_dict("records")
    if data_dict:
        collection.insert_many(data_dict)
        print("✅ Datos cargados exitosamente en MongoDB.")
    else:
        print("⚠️ No se encontraron datos para subir a MongoDB.")
except Exception as e:
    print(f"❌ Error al conectar o subir a MongoDB: {e}")