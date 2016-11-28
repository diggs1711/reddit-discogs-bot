import praw
import botSetup
import re
import discogs_auth
import getSubmissions as red

data = {}
r = botSetup.login()
red.openFileWithSavedPosts()
subreddit = red.getSubreddit(r, 'truehouse')
red.getSubmissions(subreddit)




def writePostIdsToFile():
    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")
