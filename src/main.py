from Twitter import Twitter
from time import sleep

def main():
    twitter = Twitter()
    twitter.create_tas()

    # send a good morning tweet with a picture of the sun
    sun_media_id = twitter.get_media_id("media/sun.png")

    tweet_id = twitter.create_tweet("Good morning!", sun_media_id)
    print ("Good morning tweet has been sent!")

    # delete good morning tweet
    sleep(30)
    twitter.delete_tweet(tweet_id)
    print ("Good morning tweet has been deleted!")
    
    # send a good night tweet with a picture of the moon
    moon_media_id = twitter.get_media_id("media/moon.png")

    tweet_id = twitter.create_tweet("Good night!", moon_media_id)
    print ("Good night tweet has been sent!")
    
if __name__ == "__main__":
    main()
