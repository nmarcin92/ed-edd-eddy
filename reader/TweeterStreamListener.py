import tweepy


class TweeterStreamListener(tweepy.StreamListener):

    def __init__(self, database):
        super(TweeterStreamListener, self).__init__()
        self.db = database

    def on_status(self, tweet):
        self.db.add_tweet_if_nedded(tweet)
        if hasattr(tweet, 'retweeted_status'):
            self.db.add_tweet_if_nedded(tweet.retweeted_status)

