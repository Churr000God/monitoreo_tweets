import pandas as pd
from textblob import TextBlob
from fetch_tweets import fetch_tweets_v2
import os

alcaldias = ["Iztapalapa", "Benito Juárez", "Coyoacán", "Tlalpan", "Miguel Hidalgo", "Venustiano Carranza", "Álvaro Obregón"]
servicios = ["policía", "seguridad", "tránsito", "vialidad", "guardia", "emergencia", "patrulla"]

def analizar_sentimiento(texto):
    sentimiento = TextBlob(texto)
    polaridad = sentimiento.sentiment.polarity
    if polaridad > 0.1:
        return "Positivo"
    elif polaridad < -0.1:
        return "Negativo"
    else:
        return "Neutral"

def main():
    ruta = "data/tweets_with_sentiment.csv"

    # Verificar si el archivo ya existe
    if os.path.exists(ruta):
        print("📁 Archivo ya existe. Saltando descarga.")
        return

    print("📥 Obteniendo tweets...")
    queries = ['@SSC_CDMX', '@GobCDMX', '@Alcaldia_Iztapalapa', '@Alcaldia_BJ', '@Alcaldia_Coy', '@Alcaldia_Tlalpan', '@Alcaldia_MH', '@Alcaldia_VC', '@Alcaldia_AO']
    tweets = fetch_tweets_v2(queries, max_tweets=10)

    if not tweets:
        print("❌ No se obtuvieron tweets.")
        return

    print("🧠 Enriqueciendo tweets...")
    for tweet in tweets:
        texto = tweet['Text'].lower()
        tweet['Sentimiento'] = analizar_sentimiento(tweet['Text'])
        tweet['Alcaldía'] = next((a for a in alcaldias if a.lower() in texto), None)
        tweet['Servicio'] = next((s for s in servicios if s.lower() in texto), None)

    print("💾 Guardando en 'data/tweets_with_sentiment.csv'...")
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(tweets)
    df.to_csv(ruta, index=False)

    print("✅ Proceso completado: Tweets con sentimiento y clasificación de alcaldía/servicio guardados.")

if __name__ == "__main__":
    main()