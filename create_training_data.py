import tweepy
import clean_text
import pprint

NUMBER_OF_TWEETS_CHECKED = 5

# boilerplate stuff
with open('keys.txt', 'r') as keysfile:
    keys = keysfile.readlines()
    CONSUMER_KEY = keys[0].rstrip()
    CONSUMER_SECRET = keys[1].rstrip()
    ACCESS_TOKEN = keys[2].rstrip()
    ACCESS_TOKEN_SECRET = keys[3].rstrip()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# read list of users
with open('userlist.txt', 'r') as usersfile:
    users = []
    for user in usersfile.readlines():
        users.append(user.rstrip())

# makes list of user and machine safe tweets
master_text = {}

for user in users:
    master_text[user] = []
    for tweet in api.user_timeline(user, count=NUMBER_OF_TWEETS_CHECKED, tweet_mode='extended'):
        user_safe = clean_text.make_user_safe(tweet)
        machine_safe = clean_text.make_machine_safe(tweet)
        master_text[user].append({'user_safe': user_safe, 'machine_safe': machine_safe})

print(master_text)