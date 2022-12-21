import logging

import private
import settings
import tweepy
import dataset
from textblob import TextBlob
from sqlalchemy.exc import ProgrammingError
import json

# Using TwitterAPI v2

# connect to the database to store tweets
db = dataset.connect(settings.CONNECTION_STRING)

# create a client object, pass twitter credentials to it
client = tweepy.Client(private.BEARER_TOKEN, private.TWITTER_API_KEY, private.TWITTER_API_SECRET,
                       private.TWITTER_APP_KEY, private.TWITTER_APP_SECRET)
# create an oauth handler object which will
auth = tweepy.OAuth1UserHandler(private.TWITTER_API_KEY, private.TWITTER_API_SECRET, private.TWITTER_APP_KEY,
                                private.TWITTER_APP_SECRET)
# create api object and pass the oauth handler object to it to handle credentials
api = tweepy.API(auth)


class TweetStream(tweepy.StreamingClient):        # the tweetstream class inherits from the tweepy StreamingClient class

    def on_connect(self):                   # on_connect is called upon stream connection
        print("Connected")

    def on_tweet(self, tweet):              # on_tweet handles logic as new tweets come in over the stream
        # if the tweet is a retweet, do not save it
        if tweet.retweeted:
            return
        # else move on to saving the tweet to the database
        # save the needed info to variables
        user_description = tweet.user.description
        user_location = tweet.user.location
        text = tweet.text
        username = tweet.user.screen_name
        user_created = tweet.user.created_at
        followers = tweet.user.followers_count
        id_str = tweet.id_str
        tweet_created = tweet.created_at
        retweets = tweet.retweet_count
        blob = TextBlob(text)
        sentiment = blob.sentiment
        # todo this might be an old way of doing things and have to be redone.
        table = db[settings.TABLE_NAME]

        try:
            # insert the tweet into the database as a dictionary object with all the tweet information
            table.insert(dict(
                user_description=user_description,
                user_location=user_location,
                text=text,
                username=username,
                tweet_created_date=tweet_created,
                followers=followers,
                id_str=id_str,
                user_created_date=user_created,
                retweets=retweets,
                blob=blob,
                sentiment=sentiment,
            ))
            # catch errors and log them to the consol
        except ProgrammingError as err1:
            # todo need to add logging here
            print("There was a ProgrammingError thrown, probably a problem with the database" + err1)
        except tweepy.TweepyException as err2:
            print(
                "there was a TweepyException thrown, probably a problem with twitter or the rate limit has been hit" + err2)

    def on_errors(self, err):
        print("an error occured with the tweet stream " + err)


# Create the stream object
stream = TweetStream(bearer_token=private.BEARER_TOKEN)
# add new 'rules' to filter result
for term in settings.SEARCH_TERMS:
    stream.add_rules(tweepy.StreamRule(term))
# filter the stream
stream.filter()
