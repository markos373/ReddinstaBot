
import json
import logging
import sys
from reddit import RedditAPI

CONFIGURATION_FILE_PATH = "redditapi.json"

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
    for submission in reddit_api.get_hot(subreddits,1):
        print(submission)
    

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
