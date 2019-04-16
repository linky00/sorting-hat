import tweepy
import clean_text
import pprint

NUMBER_OF_TWEETS_CHECKED = 7
HOUSE_INDEX = {"g": 0, "s": 1, "r": 2, "h": 3}

# boilerplate auth stuff
with open('keys.txt', 'r') as keys_file:
    keys = keys_file.readlines()

CONSUMER_KEY = keys[0].rstrip()
CONSUMER_SECRET = keys[1].rstrip()
ACCESS_TOKEN = keys[2].rstrip()
ACCESS_TOKEN_SECRET = keys[3].rstrip()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# read list of users
users = []

with open('userlist.txt', 'r') as users_file:
    for user in users_file.readlines():
        users.append(user.rstrip())

# makes list of user and machine safe tweets
master_text = {}

for user in users:
    master_text[user] = []
    for tweet in api.user_timeline(user, count=NUMBER_OF_TWEETS_CHECKED, tweet_mode='extended'):
        user_safe = clean_text.make_user_safe(tweet)
        machine_safe = clean_text.make_machine_safe(tweet)
        master_text[user].append({'user_safe': user_safe, 'machine_safe': machine_safe})

# make output file (this system is all temporary)
with open('output' + users[0] + '.csv', 'w+') as output_file:
    for user in master_text:
        # shove together all the machine tweets whilst printing the user ones
        long_text = ""
        print("--------------")
        for tweet in master_text[user]:
            long_text = long_text + tweet['machine_safe'] + " "
            print(tweet['user_safe'])
            print("-------")
        long_text.replace("\"", "\"\"")
        long_text = "".join(i for i in long_text if ord(i)<128)
        # make decision
        decision = ""
        while decision not in ["g", "h", "r", "s"]:
            decision = input("House:")
        print("--------------")
        # put this into the file
        print(long_text)
        output_file.write("\"" + long_text + "\", " + str(HOUSE_INDEX[decision]) + '\n')