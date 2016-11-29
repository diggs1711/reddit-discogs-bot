import praw
import obot

def login():
    r = praw.Reddit(user_agent = obot.app_ua)
    r.set_oauth_app_info(client_id = obot.app_id, client_secret = obot.app_secret, redirect_uri = obot.app_uri)
    r.refresh_access_information(obot.app_refresh)
    return r
