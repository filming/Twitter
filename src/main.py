from extra.error_handling import error_handle
from auth.create_tas import create_tas
from tweet.tweet import create_tweet

def main():
    raw_return = create_tas()
    error_handle(raw_return)
    tas = raw_return[1][0]

    tweet_message = "Hello!"
    create_tweet(tas, tweet_message)
    print ("Tweeted!")
    
    






if __name__ == "__main__":
    main()