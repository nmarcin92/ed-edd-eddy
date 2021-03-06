import tweepy
from reader.Database import Database
from reader.TweeterStreamListener import TweeterStreamListener
from auth import api

if __name__ == "__main__":
    database = Database()
    listener = TweeterStreamListener(database)
    stream = tweepy.Stream(auth=api.auth, listener=listener)
    while True:
        try:
            stream.filter(track=database.find_all_keyword())
        except Exception as e:
            print 'error'
            print e
            print "****************"
