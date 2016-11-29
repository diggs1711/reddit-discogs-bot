import os
import discogsObject
import re
import createComment
posts_replied_to = []

def openFileWithSavedPosts():
    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []
    else:
        with open("posts_replied_to.txt", "r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = filter(None, posts_replied_to)
            
def getSubreddit (r, sub):
    return r.get_subreddit(sub)

def getSubmissions(subreddit):
    for submission in subreddit.get_hot(limit=5):

        if submission.id not in posts_replied_to:
            song = submission.title
            results = discogsObject.Search(song)
            
            if (results.count != 0):
                result = discogsObject.retrieveData(results)
                print result.title
                createComment.create(submission, result)
                # posts_replied_to.append(submission.id);
            else:             
                song = re.sub("[\(\[].*?[\)\]]", "", song)
                results = discogsObject.Search(song)
                
                if results.count != 0:
                    result = discogsObject.retrieveData(results)
                    print result.title
