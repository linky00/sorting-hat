import re

def make_user_safe(tweet):
    result = tweet.full_text
    result = re.sub(r'^RT', "(RETWEETED)", result)
    if tweet.is_quote_status:
        result = re.sub(r'https:\/\/t\.co\/\w+$', "(QUOTED TWEET HERE)", result)
    if 'media' in tweet._json['entities']:
        result = re.sub(r'https:\/\/t\.co\/\w+$', "(IMAGE(S) HERE)", result)
    return result

def make_machine_safe(tweet):
    result = tweet.full_text
    result = result.replace("\n", " ")
    result = re.sub(r'RT', "RETWEETEDHERE", result)
    if tweet.is_quote_status:
        result = re.sub(r'https:\/\/t\.co\/\w+$', "QUOTEDTWEETHERE", result)
    if 'media' in tweet._json['entities']:
        result = re.sub(r'https:\/\/t\.co\/\w+$', "IMAGESHERE", result)
    return result