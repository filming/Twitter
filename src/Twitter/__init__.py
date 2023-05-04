from .auth.create_tas import create_tas
from .tweet.tweet import create_tweet
from .tweet.media import get_media_id

import sys

class Twitter():
    def __init__(self):
        self.tas = None
        self.auth_uid = 0
        self.auth_username = ""
    
    # this will end the program when the the raw_return[0] indicates an error
    def error_handle(self, raw_return):
        if raw_return[0] == 1:
            sys.exit(raw_return[1][0])

    # create twitter authorized session object
    def create_tas(self):
        raw_return = create_tas()
        self.error_handle(raw_return)

        self.tas = raw_return[1][0]
        self.auth_uid = raw_return[1][1]
        self.auth_username = raw_return[1][2]
        
    # takes a file, uploads it to twitter and returns a media id to access the file media
    def get_media_id(self, filepath):
        media_id = get_media_id(self.tas, filepath)

        return media_id
    
    # this will create a tweet, with possiblities of adding medias and replying to other tweets
    def create_tweet(self, message = "", media_ids = None, reply_ids = None):
        raw_return = create_tweet(self.tas, message, media_ids, reply_ids)
        self.error_handle(raw_return)
        tweet_id = raw_return[1][0]

        return tweet_id
    