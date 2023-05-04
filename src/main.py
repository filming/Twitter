from Twitter import Twitter

def main():
    twitter = Twitter()
    twitter.create_tas()

    # send a good morning tweet with a picture of the sun
    sun_media_id = Twitter.get_media_id("media/sun.png")

    twitter.create_tweet("Good morning!", sun_media_id)




    # send a good night tweet with a picture of the moon
    
    






if __name__ == "__main__":
    main()