import tweepy

with open('keys.txt', 'r') as keysfile:
    keys = keysfile.readlines()
    CONSUMER_KEY = keys[0].rstrip()
    CONSUMER_SECRET = keys[1].rstrip()
    ACCESS_TOKEN = keys[2].rstrip()
    ACCESS_TOKEN_SECRET = keys[3].rstrip()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

with open('userlist.txt', 'r') as usersfile:
    users = []
    for user in usersfile.readlines():
        users.append(user.rstrip())

master_text = {}

for user in users:
    for text in (tweet.text for tweet in api.user_timeline(user, count=5)):
        # user_safe = FIGURE THIS BIT OUT NEXT BASICALLY YOU NEED TO APPEND MASTER_TEXT WITH THE TWITTERUSER:{USER_SAME: TEXT, MACHINE_SAME, TEXT}
    print('\n')