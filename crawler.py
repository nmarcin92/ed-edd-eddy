from listener import *
import sys

if __name__ == "__main__":
    conn = psycopg2.connect("dbname=twitter user=postgres password=postgres")
    cur = conn.cursor()
    cur.execute("SELECT word FROM keyword")
    keywords = [k[0] for k in cur.fetchall()]


    cur.close()

    listener = TestStreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=listener)
    while True:
        try:
            stream.filter(track=keywords)
        except Exception as e:
            print e
            print 'error'
            sys.stdout.flush()
