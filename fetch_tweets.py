import tweepy
import pandas as pd
import os
import re
from dotenv import load_dotenv

#Cargar variables de entorno desde .env
load_dotenv()
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

#Inicializar cliente del API de Twitter
client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)

#Obtener los tweets de la cuenta de Twitter
def fetch_tweets_v2(queries, max_tweets=100):
    all_tweets = []
    for query in queries:
        response = client.search_recent_tweets(
            query=query,
            tweet_fields=['created_at', 'entities'],
            expansions=['author_id'],
            max_results=min(max_tweets, 100),
        )
        if response.data:
            for tweet in response.data:
                tweet_data = {
                    'Author_ID': tweet.author_id,
                    'Created_AT': tweet.created_at,
                    'Text': tweet.text,
                    'Hashtags': tweet.entities['hashtags'] if tweet.entities and 'hashtags' in tweet.entities else [],
                    'Mentions': tweet.entities['mentions'] if tweet.entities and 'mentions' in tweet.entities else [],
                }
                all_tweets.append(tweet_data)
            return all_tweets

#Palabras clave o cuentas a monitorear
queries = ['@GN_MEXICO_', '@SSPCMexico', '@SSC_CDMX', '@Claudiashein', '@GobCDMX', '@ach_CDMX', '@INEGI_INFORMA']

#ejecutar funcion
tweets_data = fetch_tweets_v2(queries)

#Crear carpeta si no existe
os.makedirs('data', exist_ok=True)

#Guardar en CVS
df = pd.DataFrame(tweets_data)
df.to_csv(os.path.join('data', 'tweets.csv'), index=False)

print("✅ Tweets guardados correctamente en 'data/tweets.csv'")
