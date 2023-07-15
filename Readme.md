You need to add your own reddit account details on a new file in the same directory called reddit_api.py to get this to run 
import praw

class RedditBot:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id='',
            client_secret='',
            user_agent='',
            username='',
            password=''
## You don't need to add the username and password for your account, unless you want to add comments or make any changes in the post.
        )
