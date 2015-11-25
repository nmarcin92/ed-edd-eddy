import psycopg2


class Database:
    def __init__(self):
        self.connection = psycopg2.connect("dbname=twitter_db user=postgres password=postgres")

    def save_sentiment(self, tweet_id, sentiment):
        cur = self.connection.cursor()
        cur.execute("""UPDATE tweet SET sentiment = %s WHERE id = %s;""", (sentiment, tweet_id))
        self.connection.commit()
        cur.close()

    def find_tweets(self):
        cur = self.connection.cursor()
        cur.execute("""SELECT id,text FROM tweet WHERE sentiment is NULL""")
        return [(t[0], t[1]) for t in cur.fetchall()]
