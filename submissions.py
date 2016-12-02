import os
import discogs
import re
import comment

POSTS = "posts_replied_to.txt"
posts_replied_to = []

def openFileWithSavedPostIds():
    if not os.path.isfile(POSTS):
        global posts_replied_to
        posts_replied_to = []
    else:
        with open(POSTS, "r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = filter(None, posts_replied_to)
            
def getSubreddit (r, sub):
    return r.get_subreddit(sub)

def getSubmissions(subreddit):
    openFileWithSavedPostIds()
    for submission in subreddit.get_hot(limit=5):
        if submission.id not in posts_replied_to:
            song = submission.title
            song = re.sub("[\(\[].*?[\)\]]", "", song)
            results = discogs.Search(song)
            
            if (results.count != 0):
                result = discogs.retrieveData(results)
                comment.create(submission, result)
                posts_replied_to.append(submission.id);
            else:             
                song = re.sub("[\(\[].*?[\)\]]", "", song)
                results = discogs.Search(song)
                
                if results.count != 0:
                    result = discogs.retrieveData(results)
