import tweepy
import clean_text
import easygui

INTRO_MESSAGE = """Hi! Thanks for helping with this project. This is an extremely dumb idea, but it should be some fun.

For each user, you're going to see seven tweets, separated by '----------'. If you don't see them all at first, you should be able to scroll down. (You'll need to scroll this text box as well...)

You'll then be asked to select an appropriate house. Please use your intuition and decide based on what makes sense to YOU (though do go reread the house descriptions on some wiki so that we're all on the same page).

Try to avoid ignoring a house or picking it constantly, however, don't let this get in the way of your COLD IRON FIST OF TRUTH.

Retweets will start with '(RETWEETED)', and if the tweet is quoting another or has media attatched it will end in '(QUOTED TWEET HERE)' or '(IMAGE(S) HERE)' respectively. Sadly, I can't display them normally, so you'll just have to guess from context.

When you're done, please send the created .csv file(s) back to me!

Start by selecting one of the userlist files I sent you..."""

FINISHED_MESSAGE = """Done! If you have more userlists to go, just reload this software, otherwise just send me your .csv file(s). Oh, and the name you'd like to be credited under, as well as some web presence if you want!

Thank you for the help!"""

NUMBER_OF_TWEETS_CHECKED = 7
HOUSE_INDEX = {"Gryffindor": 0, "Slytherin": 1, "Ravenclaw": 2, "Hufflepuff": 3}

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

# give intro message
easygui.msgbox(INTRO_MESSAGE, "Yo!")

# read list of users
users = []

with open(easygui.fileopenbox(), 'r') as users_file:
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
        gui_text = "----------"
        long_text = ""
        for tweet in master_text[user]:
            gui_text = gui_text + "\n" + tweet['user_safe'] + "\n----------"
            long_text = long_text + tweet['machine_safe'] + " "
        long_text.replace("\"", "\"\"")
        # make decision
        decision = easygui.buttonbox(gui_text, "Classify these tweets", ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"])
        # put this into the file
        output_file.write("\"" + long_text + "\", " + str(HOUSE_INDEX[decision]) + '\n')

# finished message
easygui.msgbox(FINISHED_MESSAGE, "Bye!")