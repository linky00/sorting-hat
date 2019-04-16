import tweepy

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

user_pages = tweepy.Cursor(api.followers, screen_name="Jack").pages()

for page in user_pages:
    for user in page:
        print(user.screen_name)
    input()