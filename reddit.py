from reddit_api import RedditBot

bot = RedditBot()

def get_subreddit_posts(subreddit_name):
    subreddit = bot.reddit.subreddit(subreddit_name)
    posts = subreddit.top(limit=25)
    return posts

subreddit_name = "sunraybee"  # Replace with the desired subreddit name
posts = get_subreddit_posts(subreddit_name)

for post in posts:
    print("Title:", post.title)
