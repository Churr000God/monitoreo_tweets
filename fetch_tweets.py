import tweepy
import pandas as pd
import os
import time
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# Inicializar cliente del API de Twitter
client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)

# Listas de referencia
alcaldias = ["Iztapalapa", "Benito Juárez", "Coyoacán", "Tlalpan", "Miguel Hidalgo", "Venustiano Carranza", "Álvaro Obregón"]
delitos = ["robo", "asalto", "homicidio", "violación", "secuestro", "extorsión", "balacera", "feminicidio"]

# Función para obtener tweets y enriquecerlos
def fetch_tweets_v2(queries, max_tweets=10):
    all_tweets = []
    for query in queries:
        response = client.search_recent_tweets(
            query=query,
            tweet_fields=['created_at', 'entities'],
            expansions=['author_id'],
            max_results=min(max_tweets, 10),
        )
        if response.data:
            for tweet in response.data:
                text = tweet.text.lower()

                # Enriquecimiento
                alcaldia_encontrada = next((a for a in alcaldias if a.lower() in text), None)
                delito_encontrado = next((d for d in delitos if d.lower() in text), None)

                tweet_data = {
                    'Author_ID': tweet.author_id,
                    'Created_AT': tweet.created_at,
                    'Text': tweet.text,
                    'Alcaldía': alcaldia_encontrada,
                    'Delito': delito_encontrado,
                    'Hashtags': tweet.entities['hashtags'] if tweet.entities and 'hashtags' in tweet.entities else [],
                    'Mentions': tweet.entities['mentions'] if tweet.entities and 'mentions' in tweet.entities else [],
                }
                all_tweets.append(tweet_data)
        time.sleep(10)  # Espera 10 segundos entre cada query para evitar límite
    return all_tweets

# Queries (cuentas a monitorear)
queries = ['@GN_MEXICO_', '@SSPCMexico', '@SSC_CDMX', '@Claudiashein', '@GobCDMX', '@ach_CDMX', '@INEGI_INFORMA']

# Ejecutar
tweets_data = fetch_tweets_v2(queries)
os.makedirs('data', exist_ok=True)
df = pd.DataFrame(tweets_data)
df.to_csv(os.path.join('data', 'tweets.csv'), index=False)

print("✅ Tweets enriquecidos y guardados correctamente en 'data/tweets.csv'")