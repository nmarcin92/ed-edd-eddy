import psycopg2


class Database:
    def __init__(self):
        self.connection = psycopg2.connect("dbname=twitter user=postgres password=lolol123")

    def get_users_in_reply_to_connection(self, limit):
        cur = self.connection.cursor()
        cur.execute("""
            SELECT u.username, u2.username FROM twitter_user u
            JOIN tweet t ON t.user_id = u.id
            JOIN tweet t2 ON t2.id = t.in_reply_to
            JOIN twitter_user u2 ON t2.user_id = u2.id
            ORDER BY u.followers_count DESC
            LIMIT %s""", (limit, ))
        return cur.fetchall()

    def get_users_retweet_connection(self, limit):
        cur = self.connection.cursor()
        cur.execute("""
            SELECT u.username, u2.username FROM twitter_user u
            JOIN tweet t ON t.user_id = u.id
            JOIN tweet t2 ON t2.id = t.retweet_id
            JOIN twitter_user u2 ON t2.user_id = u2.id
            ORDER BY u.followers_count DESC
            LIMIT %s""", (limit, ))
        return cur.fetchall()

    def get_users_retweet_or_reply_to_connection(self, limit):
        cur = self.connection.cursor()
        cur.execute("""
            SELECT u.username, u2.username FROM twitter_user u
            JOIN tweet t ON t.user_id = u.id
            JOIN tweet t2 ON t2.id = t.retweet_id or t2.id = t.in_reply_to
            JOIN twitter_user u2 ON t2.user_id = u2.idORDER BY u.followers_count DESC
            LIMIT %s""", (limit, ))
        return cur.fetchall()

