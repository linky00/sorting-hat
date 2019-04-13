import tweepy

with open('keys', 'r') as keysfile:
    keys = keysfile.readlines()
    CONSUMER_KEY = keys[0].rstrip()
    CONSUMER_SECRET = keys[1].rstrip()
    ACCESS_TOKEN = keys[2].rstrip()
    ACCESS_TOKEN_SECRET = keys[3].rstrip()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)