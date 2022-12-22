import dataset
import tweepy
from sqlalchemy.exc import ProgrammingError

import private
import settings

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


class TweetStream(tweepy.StreamingClient):  # the tweetstream class inherits from the tweepy StreamingClient class

    def on_connect(self):  # on_connect is called upon stream connection
        print("Connected")
        db.create_table(settings.TABLE_NAME)  # create the table in db if it does not exist already

    def on_tweet(self, tweet):      # on_tweet handles logic as new tweets come in over the stream
        tweet_text = tweet.text     # save the text of the tweet
        tweet_id = str(tweet.id)    # save the tweet id
        entry = dict(
            tweet_text=tweet_text,
            tweet_id=tweet_id,
            consumed=False          # add a consumed=false field to signal the service that will process the info later
        )
        table = db[settings.TABLE_NAME]
        try:
            # insert the tweet into the database as a dictionary object with all the tweet information
            table.insert(entry)
            # catch errors and log them to the console
        except ProgrammingError as err1:
            print("There was a ProgrammingError thrown, probably a problem with the database" + err1)
        except tweepy.TweepyException as err2:
            print(
                "there was a TweepyException thrown, probably a problem with twitter or the rate limit has been hit" + err2)

    # an on_tweet func with no db insert for testing
    # def on_tweet(self, tweet):
    #     print(tweet)
    #     time.sleep(2)

    def on_errors(self, err):
        print("an error occured with the tweet stream " + err)


# Create the stream object
stream = TweetStream(bearer_token=private.BEARER_TOKEN)
current_rules = stream.get_rules().data  # get current rules

if current_rules is not None:           # if there are current rules in place...
    for rule in current_rules:          # iterate through them...
        stream.delete_rules(rule.id)    # and delete them

# add new rules to filter result
for stream_rule in settings.STREAM_FILTER_RULES:
    stream.add_rules(tweepy.StreamRule(stream_rule))

# filter the stream, the stream of tweets filtered by the stream r
stream.filter()


