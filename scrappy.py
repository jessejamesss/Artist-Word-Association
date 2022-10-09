import tweepy
import config

# config = configparser.ConfigParser()
# config.read('config.ini')

# apiKey = config['twitter']['apiKey']
# apiKeySecret = config['twitter']['apiKeySecret']
# accessToken = config['twitter']['accessToken']
# accessTokenSecret = config['twitter']['accessTokenSecret']

# Functions
def getClient():
    client = tweepy.Client(bearer_token = config.bearerToken, 
                       consumer_key = config.apiKey,
                       consumer_secret = config.apiKeySecret,
                       access_token = config.accessToken,
                       access_token_secret = config.accessTokenSecret)
            
    return client

def getUserInfo():
    client = getClient()
    user = client.get_user(username = 'jessejames_____')
    return user.data.id


# Authentication
auth = tweepy.OAuthHandler(config.apiKey, config.apiKeySecret)
auth.set_access_token(config.accessToken, config.accessTokenSecret)

api = tweepy.API(auth)

# Get Client and User
client = getClient()
user = getUserInfo()


tweets = client.get_users_tweets(user)
print(tweets)
# user = 'jessejames_____'
# limit = 100

# tweets = api.get_users_tweets(user)

# for tweet in tweets:
#     print(tweet.full_text)
