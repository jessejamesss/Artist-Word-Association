import tweepy
import config
import pandas as pd

# Functions
def getClient():
    client = tweepy.Client(bearer_token = config.bearerToken, 
                       consumer_key = config.apiKey,
                       consumer_secret = config.apiKeySecret,
                       access_token = config.accessToken,
                       access_token_secret = config.accessTokenSecret)
            
    return client

def getUserInfo(handle):
    client = getClient()
    user = client.get_user(username = handle)
    return user.data.id

def getTweetReplies(artist_handle, tweetID):
    repliesArray = []

    for reply in tweepy.Cursor(api.search_tweets, q = 'to:{}'.format(artist_handle), since_id = tweetID).items(50):
        if hasattr(reply, 'in_reply_to_status_id_str'):
            if reply.in_reply_to_status_id == tweetID:
                repliesArray.append(reply)

# Tuple of Handles
testHandles = tuple()
testHandles = ('jessejames_____', 'arlenelmao')

# Authentication
auth = tweepy.OAuthHandler(config.apiKey, config.apiKeySecret)
auth.set_access_token(config.accessToken, config.accessTokenSecret)

api = tweepy.API(auth)

# Get Client and User
client = getClient()
# user = getUserInfo()

columns = ['Name', 'Handle', 'Type', 'Tweet Body']

# Use pagination to get user tweets
for handle in testHandles:
    user = getUserInfo(handle)
    paginator = tweepy.Paginator(client.get_users_tweets, user, exclude = 'retweets',
                                 max_results = 100)

    for page in paginator:
        #print(page)
        for tweet in page.data:
            replies = getTweetReplies(handle, tweet.id)
            print(replies)
