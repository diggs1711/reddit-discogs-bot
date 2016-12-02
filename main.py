import praw
import bot_setup
import re
import discogs_auth
import submissions

TEST_SUBREDDIT = 'testmyappdiscogslink'
SUBREDDIT = 'truehouse'

def writePostIdsToFile():
    with open("posts_replied_to.txt", "w") as f:
        for post_id in submissions.posts_replied_to:
            f.write(post_id + "\n")

def main():
    submissions.openFileWithSavedPostIds()
   
    reddit = bot_setup.login()

    subreddit = submissions.getSubreddit(reddit, TEST_SUBREDDIT)
    submissions.getSubmissions(subreddit)

    writePostIdsToFile()

if __name__ == '__main__':
    main()

