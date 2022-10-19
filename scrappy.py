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

    return user


# Dictionary of artist name and their Twitter handle
artistDictionary = {'Jesse James' : 'jessejames_____', 'Arlene' : 'arlenelmao'}

# Authentication
auth = tweepy.OAuthHandler(config.apiKey, config.apiKeySecret)
auth.set_access_token(config.accessToken, config.accessTokenSecret)

api = tweepy.API(auth)

# Get Client
client = getClient()

# Create columns for csv file
artistColumns = ['Name', 'Handle', 'Username', 'Artist ID', 'Type', 'Tweet ID', 'Tweet Text']
artistTweetsData = []
mentionsColumns = ['RTA Name', 'RTA Handle', 'RTA Username', 'RTA ID', 'Handle', 'Username', 'ID', 'Type', 'Tweet ID', 'Tweet Text']
artistMentionsData = []

# Use pagination to get user tweets
for key in artistDictionary:
    user = getUserInfo(artistDictionary[key])
    artistName = key
    artistHandle = user.data.username
    artistUsername = user.data.name
    artistID = user.data.id
    type = 0

    tweetsPaginator = tweepy.Paginator(client.get_users_tweets, artistID, exclude = 'retweets',
                                       max_results = 100)

    for page in tweetsPaginator:
        for tweet in page.data:
            tweetID = tweet.id
            tweetText = tweet.text

            artistTweetsData.append([artistName, artistHandle, artistUsername, artistID, type, tweetID, tweetText])

for key in artistDictionary:
    user = getUserInfo(artistDictionary[key])
    artistName = key
    artistHandle = user.data.username
    artistUsername = user.data.name
    artistID = user.data.id
    type = 1
    
    mentionsPaginator = tweepy.Paginator(client.get_users_mentions, artistID, 
                                         max_results = 100)

    for page in mentionsPaginator:
        for mention in page.data:
            mentionID = mention.id
            mentionText = mention.text

            mentionData = client.get_tweet(511651662461952001, expansions='author_id', 
                                           user_fields=['id','name', 'username'])

            mentions = mentionData.includes['users']

            mentionUsername = mentionData.includes['users'].name
            mentionHandle = mentionData.includes['users'].username
            mentionUserID = mentionData.includes['users'].id

            artistMentionsData.append([artistName, artistHandle, artistUsername, artistID, mentionHandle, mentionUsername, mentionUserID, type, mentionID, mentionText])

artist_df = pd.DataFrame(artistTweetsData, columns=artistColumns)
mentions_df = pd.DataFrame(artistMentionsData, columns=mentionsColumns)

artist_df.to_csv('artist_tweets.csv')
mentions_df.to_csv('artist_mentions.csv')


