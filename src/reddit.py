
#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt

valid_types = ["jpg","png"]

class RedditAPI:

    def __init__(self,client_id ,client_secret,user_agent):
        self.api = praw.Reddit(client_id=client_id, \
                     client_secret= client_secret, \
                     user_agent=user_agent, \
                         )

    def get_hot(self,subreddits, N):
        post_info = []
        for subreddit in subreddits:
            
            topN = self.api.subreddit(subreddit).hot(limit=N)
            for post in topN:
                post_info.append((post.title,post.url))
        return post_info