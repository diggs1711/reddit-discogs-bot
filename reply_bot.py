import praw
import bot_setup
import re
import discogs_auth
import submissions as red

test = 'testmyappdiscogslink'
sub = 'truehouse'

def writePostIdsToFile():
    with open("posts_replied_to.txt", "w") as f:
        for post_id in red.posts_replied_to:
            f.write(post_id + "\n")
            
data = {}
r = bot_setup.login()
red.openFileWithSavedPosts()
subreddit = red.getSubreddit(r, test)
red.getSubmissions(subreddit)

writePostIdsToFile()


