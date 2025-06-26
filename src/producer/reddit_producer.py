import praw
import configparser
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

# Stream de nuevos posts en r/argentina
subreddit = reddit.subreddit('argentina')

print("Iniciando stream...")
for submission in subreddit.stream.submissions(skip_existing=True):
    post = {
        "id": submission.id,
        "title": submission.title,
        "created_utc": datetime.utcfromtimestamp(submission.created_utc).isoformat(),
        "author": str(submission.author),
        "url": submission.url,
        "text": submission.selftext
    }
    print(post)  # Aquí podrías hacer: enviar a Kinesis / guardar en S3 / etc.
