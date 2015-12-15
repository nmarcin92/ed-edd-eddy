import psycopg2


class Database:
    def __init__(self):
        self.connection = psycopg2.connect("dbname=twitter user=postgres password=lolol123")
        cur = self.connection.cursor()
        cur.execute("""SELECT category FROM category""")
        self.categories = [c[0] for c in cur.fetchall()]
        cur.close()

    def find_tweets_by_category(self, category, start_date, end_date):
        cur = self.connection.cursor()
        cur.execute("""SELECT t.id, t.date, t.sentiment FROM tweet t
                     join category c on t.category = c.id
                     where c.category = %s
                     and t.date>=%s and t.date<=%s""", (category, start_date, end_date))
        return [(t[0], t[1], t[2]) for t in cur.fetchall()]

    def find_all_tweets(self, start_date, end_date):
        cur = self.connection.cursor()
        cur.execute("""SELECT t.id, t.date FROM tweet t
                     where t.date>=%s and t.date<=%s""", (start_date, end_date))
        return [(t[0], t[1]) for t in cur.fetchall()]

    def find_tweets_by_username(self, username, start_date, end_date):
        cur = self.connection.cursor()
        cur.execute("""SELECT t.id, t.date, t.sentiment FROM tweet t
                     JOIN twitter_user u on t.user_id = u.id
                     where u.username = %s
                     and t.date>=%s and t.date<=%s""", (username, start_date, end_date))
        return [(t[0], t[1], t[2]) for t in cur.fetchall()]

    def find_all_categories(self):
        return self.categories
