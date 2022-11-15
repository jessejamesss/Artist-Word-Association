# Imports
import tweepy
import config
import json
import csv
from csv import writer

# Functions


# Driver code
if __name__ == '__main__':

    # Define API Authentication
    auth = tweepy.OAuthHandler(config.apiKey, config.apiKeySecret)
    auth.set_access_token(config.accessToken, config.accessTokenSecret)

    api = tweepy.API(auth,wait_on_rate_limit=True)


    # Read artist name and their handle from CSV file
    # and store them in a dictionary
    reader = csv.reader(open('ArtistList.csv', 'r'))
    artistDictionary = {}

    for row in reader:
        k, v = row
        artistDictionary[k] = v

        

    # artistDictionary = ['@omarapollo']


    # Collect all of an artist's tweets
    # for artist in artistDictionary:
    #     artist_timeline_pages = tweepy.Cursor(api.user_timeline, screen_name=artist,
    #                                           exclude_replies=False, include_rts=False).pages(1)

    #     for page in artist_timeline_pages:
    #         print(page)

    for artist in artistDictionary:
        print("Start Artist: " + artist)
        artist_timeline_pages = tweepy.Cursor(api.user_timeline, screen_name=artistDictionary[artist],
                                              exclude_replies=False, include_rts=False).pages()

        # artist = artist_timeline_pages[0]
        # json_str = json.dumps(artist._json)
        # print(json_str)
        for page in artist_timeline_pages:
            for data in page:
                with open('data.json', 'a', encoding='utf-8') as f:
                    json.dump(data._json, f, ensure_ascii=False, indent=4)
        print("Done Artist: " + artist)



    