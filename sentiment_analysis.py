import pandas as pd
from textblob import TextBlob
import os

# Leer datos procesados
df = pd.read_csv('data/processed_tweets.csv')

# Función para obtener polaridad
def obtener_sentimiento(texto):
    analisis = TextBlob(str(texto))
    polaridad = analisis.sentiment.polarity
    if polaridad > 0.1:
        return 'Positivo'
    elif polaridad < -0.1:
        return 'Negativo'
    else:
        return 'Neutral'

# Aplicar la función al texto
df['Sentimiento'] = df['Text'].apply(obtener_sentimiento)

# Guardar los resultados
os.makedirs('data', exist_ok=True)
df.to_csv('data/tweets_with_sentiment.csv', index=False)

print("✅ Datos con análisis de sentimiento guardados en 'data/tweets_with_sentiment.csv'")
