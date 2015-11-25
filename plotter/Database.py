import psycopg2


class Database:
    def __init__(self):
        self.connection = psycopg2.connect("dbname=twitter_db user=postgres password=postgres")

    def find_tweets_by_category(self, category, start_date, end_date):
        cur = self.connection.cursor()
        cur.execute("""SELECT t.id, t.date, t.sentiment FROM tweet t
                     join category c on t.category = c.id
                     where c.category = %s
                     and t.date>=%s and t.date<=%s""", (category, start_date, end_date))
        return [(t[0], t[1], t[2]) for t in cur.fetchall()]
