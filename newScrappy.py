import tweepy
import config
import sys
import json
import csv
import time


auth = tweepy.OAuthHandler(config.apiKey, config.apiKeySecret, config.accessToken, config.accessTokenSecret)
auth.set_access_token(config.accessToken, config.accessTokenSecret)

api = tweepy.API(auth, wait_on_rate_limit=True)

client = tweepy.Client(config.bearerToken, config.apiKey, config. apiKeySecret, config.accessToken, config.accessTokenSecret)


filters = []
filename = open('ArtistList.csv', 'r')
file = csv.DictReader(filename)
for col in file:
    filters.append(col['Filters'])

class MyStream(tweepy.StreamingClient):
    def on_connect(self):
        print('Connected')
    
    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            print(tweet)
    
    def on_data(self, data):
            print(data)

stream = MyStream(bearer_token=config.bearerToken)

for term in filters:
    stream.add_rules(tweepy.StreamRule(term))

stream.filter(tweet_fields=["referenced_tweets"])
