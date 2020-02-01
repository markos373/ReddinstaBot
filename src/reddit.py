
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
        post_info = set()
        
        for subreddit in subreddits:
            current_bound = 5
            imgs_found = 0
            while imgs_found < N:
                topN = self.api.subreddit(subreddit).hot(limit=current_bound)
                for post in topN:
                    found_n = False
                    for ext in valid_types:
                        if ext in post.url:
                            post_info.add((post.title,post.url))
                            imgs_found += 1
                            if imgs_found == N:
                                found_n = True
                                break
                    if found_n:
                        break
                            
                current_bound += 5

        return post_info
