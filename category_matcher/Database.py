import psycopg2


class Database:
    def __init__(self):
        self.connection = psycopg2.connect("dbname=twitter_db user=postgres password=postgres")

    def find_tweets_ids(self):
        cur = self.connection.cursor()
        cur.execute("""SELECT t.id FROM tweet t""")
        return [(t[0]) for t in cur.fetchall()]

    def find_categories_for_tweet(self, tweet_id):
        cur = self.connection.cursor()
        cur.execute("""SELECT c.id FROM category c
                      JOIN category_keyword ck ON ck.category = c.id
                      JOIN keyword_tweet kt ON kt.keyword = ck.keyword
                      where kt.tweet = %s""", (tweet_id,))
        return [t[0] for t in cur.fetchall()]

    def assign_category(self, t_id, category):
        cur = self.connection.cursor()
        cur.execute("""UPDATE tweet SET category = %s WHERE id = %s;""", (category, t_id))
        self.connection.commit()
        cur.close()
