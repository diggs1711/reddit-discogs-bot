import praw
from prawoauth2 import PrawOAuth2Server
user_agent = 'discogs_bot'
reddit_client = praw.Reddit(user_agent)
scopes = ['read']

app_key = 'zV9FatAYYMwFuw'
app_secret = 'iU0N6vOXINJVG9bkcrWG3p9Atmw'

oauthserver = PrawOAuth2Server(reddit_client, app_key, app_secret, state=user_agent, scopes=scopes)

