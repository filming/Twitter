from Twitter import Twitter

def main():
    twitter = Twitter()
    twitter.create_tas()

    # send a good morning tweet with a picture of the sun
    sun_media_id = twitter.get_media_id("media/sun.png")

    tweet_id = twitter.create_tweet("Good morning!", sun_media_id)
    print ("Good morning tweet has been sent!")

    # delete good morning tweet
    
    

    
    


    # send a good night tweet with a picture of the moon
    
    






if __name__ == "__main__":
    main()