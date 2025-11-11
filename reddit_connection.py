import praw
from praw import Reddit

client_id = "LhEYyHU_jPOmydQBHIC2XQ"
client_secret = "ewlC3-D0kYietswdRZDI58-eXmJ-eA"
user_agent = "myProjectApp:v1.0 (by u/Artemis1914)"

reddit = praw.Reddit(client_id=client_id,
                    client_secret=client_secret,
                    user_agent=user_agent
)

posts = reddit.subreddit("learnpython").hot(limit=5)

for post in posts:
    post = vars(post)
    print(post)