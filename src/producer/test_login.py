import praw
import configparser

config = configparser.ConfigParser()
config.read('src/producer/config.ini')

reddit = praw.Reddit(
    client_id=config['reddit']['client_id'],
    client_secret=config['reddit']['client_secret'],
    username=config['reddit']['username'],
    password=config['reddit']['password'],
    user_agent=config['reddit']['user_agent']
)

print("Usuario autenticado:", reddit.user.me())
