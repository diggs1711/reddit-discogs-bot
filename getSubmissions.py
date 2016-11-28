import os
import discogsObject
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
            results = discogsObject.Search(submission.title)
            if (results.count != 0):
                result = discogsObject.retrieveData(results)
                #print result.title
                # posts_replied_to.append(submission.id);
            else:
                songs = submission.title.split(' - ')
                
                for song in songs:
                    results = discogsObject.Search(song)
                
                if results.count != 0:
                    print "HEllo"
                else:
         
                    songWithoutLabelOrYear = song.split(' [')[0]
                    results = discogsObject.Search(songWithoutLabelOrYear)
                    #print results.count