
import json
import logging
import sys
import os
import requests
from reddit import RedditAPI

CONFIGURATION_FILE_PATH = "redditapi.json"
MEDIA_DIR               = "media/"

def create_post_queue(submissions):
    post_queue = []
    for submission in submissions: 
        fpath = os.path.join(MEDIA_DIR,submission[1].split('/')[-1])
        f = open(fpath,'wb')
        f.write(requests.get(submission[1]).content)
        f.close()          #(fpath, submission)
        post_queue.append((fpath,submission[0]))
    return post_queue
        
def run_bot(post_queue):
    for post in post_queue:
        #currently have post_queue, figure out resetting logic



if __name__ == "__main__":

    logging.basicConfig(filename="python.log", filemode="w", format="[%(asctime)s] %(levelname)s: %(message)s", level=logging.INFO)
    logger = logging.getLogger()

    key_id = secret_key = ""
    try:
        file          = open(CONFIGURATION_FILE_PATH, "r")
        data          = json.load(file)
        client_id     = data["config"]["client_id"]
        client_secret = data["config"]["client_secret"] 
        user_agent    = data["config"]["user_agent"] 
        subreddits    = data["config"]["subreddits"]
    except:
        logger.fatal("ERROR: failed to extract keys from configuration file located at \"%s\"" % CONFIGURATION_FILE_PATH)
        sys.exit()

    reddit_api = RedditAPI(client_id ,client_secret,user_agent)
    submissions = reddit_api.get_hot(subreddits,1)
    create_post_queue(submissions)
    
    
    logging.shutdown()
'''
0. If tobe_posted.txt is empty:
    1. Build set of top 2 posts from 5 different subreddits
        -Only grab imgur / reddit links
    2. Load into text file as list
1. If not empty:
    1. Post first line of tobe_posted.txt
    2. Remove line from file
    3. Sleep N seconds


'''
