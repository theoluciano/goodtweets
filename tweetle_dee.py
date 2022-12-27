import pandas as pd
import tweepy 
import quote_scraper

from tokens import twitter_secrets as ts

consumer_key = ts.CONSUMER_KEY
consumer_secret = ts.CONSUMER_SECRET
access_token = ts.ACCESS_TOKEN
access_secret = ts.ACCESS_SECRET

#Authenticating to access the twitter API
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)

# Define the tweet text
tweet = quote_scraper.main()

# Generate text tweet
api.update_status(tweet)
