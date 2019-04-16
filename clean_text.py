import re

def make_user_safe(tweet):
    result = retweet_fixed(tweet)
    result = "".join(i for i in result if ord(i)<128)
    result = re.sub(r'^RT', "(RETWEETED)", result)
    if tweet.is_quote_status:
        result = re.sub(r'https:\/\/t\.co\/\w+$', "(QUOTED TWEET HERE)", result)
    if 'media' in tweet._json['entities']:
        result = re.sub(r'https:\/\/t\.co\/\w+$', "(IMAGE(S) HERE)", result)
    return result

def make_machine_safe(tweet):
    result = retweet_fixed(tweet)
    result = "".join(i for i in result if ord(i)<128)
    result = result.replace("\n", " ")
    result = re.sub(r'RT', "RETWEETEDHERE", result)
    if tweet.is_quote_status:
        result = re.sub(r'https:\/\/t\.co\/\w+$', "QUOTEDTWEETHERE", result)
    if 'media' in tweet._json['entities']:
        result = re.sub(r'https:\/\/t\.co\/\w+$', "IMAGESHERE", result)
    return result

def retweet_fixed(tweet):
    if 'retweeted_status' in tweet._json:
        return "RT @" + tweet._json['retweeted_status']['user']['screen_name'] + ": " + tweet._json['retweeted_status']['full_text']
    else:
        return tweet.full_text
