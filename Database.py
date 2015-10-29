import psycopg2


class Database:
    def __init__(self):
        self.connection = psycopg2.connect("dbname=twitter user=postgres password=lolol123")
        cur = self.connection.cursor()
        cur.execute("""SELECT id,word FROM keyword""")
        self.keywords = [(k[0], k[1]) for k in cur.fetchall()]
        cur.execute("""SELECT id,word FROM sentiment""")
        self.sentiment_words = [(s[0], s[1]) for s in cur.fetchall()]
        cur.close()

    def find_all_keyword(self):
        return [k[1] for k in self.keywords]

    def add_tweet_if_nedded(self, tweet):
        if self.has_tweet(tweet.id_str):
            self.update_retweet_count(tweet)
            return
        cur = self.connection.cursor()
        self.add_user_if_needed(tweet.user)
        localization = str(tweet.coordinates) if tweet.coordinates is not None else None
        retweet_id = tweet.retweeted_status.id_str if hasattr(tweet, 'retweeted_status') else None
        cur.execute(
            """INSERT INTO tweet (id, user_id, text, date, localization, retweet_count, retweet_id) values (%s, %s, %s, %s, %s, %s, %s);""",
            (tweet.id_str, tweet.user.id_str, tweet.text, tweet.created_at, localization, tweet.retweet_count, retweet_id)
        )
        self.find_keyword_in_tweet(cur, tweet.id_str, tweet.text)
        self.find_sentiment_word_in_tweet(cur, tweet.id_str, tweet.text)
        if hasattr(tweet.entities, 'hashtags'):
            self.add_tweet_hashtags(cur, tweet.id_str, tweet.entities.hashtags)
        if hasattr(tweet.entities, 'user_mentions'):
            self.add_user_mentions(cur, tweet.id_str, tweet.entities.user_mentions)
        self.connection.commit()
        cur.close()

    def add_user_mentions(self, cursor, tweet_id, user_mentions):
        for um in user_mentions:
            self.add_user_basic_info_if_needed(cursor, um)
            cursor.execute("""INSERT INTO mention (user, tweet) values (%s, %s);""", (um.id_str, tweet_id))

    def find_keyword_in_tweet(self, cursor, tweet_id, text):
        for k in self.keywords:
            if k[1] in text:
                cursor.execute(
                    """INSERT INTO keyword_tweet (keyword, tweet) values (%s, %s);""", (k[0], tweet_id))

    def find_sentiment_word_in_tweet(self, cursor, tweet_id, text):
        splitted_text = text.split()
        underline_text = "_".join(splitted_text)
        sents = []
        for s in self.sentiment_words:
            if "_" not in s[1]:
                for word in splitted_text:
                    if s[1] == word and s[0] not in sents:
                        sents.append(s[0])
            else:
                if s[1] in underline_text and s[0] not in sents:
                    sents.append(s[0])
        for s in sents:
            cursor.execute("""INSERT INTO sentiment_tweet (sentiment, tweet) values (%s, %s);""", (s, tweet_id))

    def add_tweet_hashtags(self, cursor, tweet_id, hashtags):
        for ht in hashtags:
            ht_id = self.add_hashtag_if_need(cursor, ht)
            cursor.execute("""INSERT INTO hashtag_tweet (hashtag, tweet) values (%s, %s);""", (ht_id, tweet_id))

    def add_hashtag_if_need(self, cursor, hashtag):
        cursor.execute("""SELECT id FROM hashtag WHERE text = %s""", (hashtag.text, ))
        rows = cursor.fetchall()
        if len(rows) == 0:
            return self.add_hashtag(cursor, hashtag)
        return rows[0][0]

    def add_hashtag(self, cursor, hashtag):
        cursor.execute("""INSERT INTO hashtag (text) values (%s)""", (hashtag.text, ))
        return self.add_hashtag_if_need(cursor, hashtag)

    def update_retweet_count(self, tweet):
        cur = self.connection.cursor()
        cur.execute("""UPDATE tweet SET retweet_count = %s WHERE id = %s;""", (tweet.retweet_count, tweet.id_str))
        self.connection.commit()
        cur.close()

    def add_user_if_needed(self, user):
        cur = self.connection.cursor()
        cur.execute("""SELECT id FROM twitter_user WHERE id = %s""", (user.id_str, ))
        rows = cur.fetchall()
        if len(rows) == 0:
            self.add_user(cur, user)
        else:
            self.update_user(cur, user)
        self.connection.commit()
        cur.close()

    @staticmethod
    def add_user_basic_info_if_needed(cursor, user):
        cursor.execute("""SELECT id FROM twitter_user WHERE id = %s""", (user.id_str, ))
        rows = cursor.fetchall()
        if len(rows) == 0:
            cursor.execute(
                """INSERT INTO twitter_user (id, username) VALUES (%s, %s)""", (user.id_str, user.screen_name))

    @staticmethod
    def add_user(cursor, user):
        cursor.execute(
            """INSERT INTO twitter_user (id, username, followers_count, friends_count, statuses_count, created_date) VALUES (%s, %s, %s, %s, %s, %s)""",
            (user.id_str, user.screen_name, user.followers_count, user.friends_count, user.statuses_count, user.created_at))

    @staticmethod
    def update_user(cursor, user):
        cursor.execute(
            """UPDATE twitter_user SET followers_count = %s, friends_count = %s, statuses_count = %s, created_date = %s WHERE id = %s""",
            (user.followers_count, user.friends_count, user.statuses_count, user.created_at, user.id_str))

    def has_tweet(self, tweet_id):
        cur = self.connection.cursor()
        cur.execute("""SELECT id FROM tweet WHERE id = %s""", (tweet_id, ))
        rows = cur.fetchall()
        existence = len(rows) > 0
        cur.close()
        return existence
