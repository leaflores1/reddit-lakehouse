import praw
import configparser
import boto3
import json
from datetime import datetime

# Leer configuración
config = configparser.ConfigParser()
config.read('src/producer/config.ini')

reddit = praw.Reddit(
    client_id=config['reddit']['client_id'],
    client_secret=config['reddit']['client_secret'],
    username=config['reddit']['username'],
    password=config['reddit']['password'],
    user_agent=config['reddit']['user_agent']
)

# Inicializar sesión AWS con perfil personalizado
session = boto3.Session(profile_name="reddit-dev", region_name="us-east-2")
kinesis = session.client("kinesis")
stream_name = "reddit-stream"

# Elegir subreddit
subreddit = reddit.subreddit('worldnews')

print("Iniciando stream y envío a Kinesis...")

# ✅ Enviar cada post a Kinesis
for submission in subreddit.stream.submissions(skip_existing=True):
    post = {
        "id": submission.id,
        "title": submission.title,
        "created_utc": datetime.utcfromtimestamp(submission.created_utc).isoformat(),
        "author": str(submission.author),
        "url": submission.url,
        "text": submission.selftext
    }

    print(f"Enviando: {post['title'][:60]}...")
    print("Enviando a Kinesis...")
    kinesis.put_record(
        StreamName=stream_name,
        Data=json.dumps(post),
        PartitionKey=post["id"]
    )
