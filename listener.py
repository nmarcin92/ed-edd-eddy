import tweepy
import psycopg2
from objects import *
from auth import api

class TestStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        conn = psycopg2.connect("dbname=twitter user=postgres password=postgres")
        cur = conn.cursor()
        user_id = self.get_user_id(conn, status.user)
        if status.coordinates != None:
            print status.coordinates

        cur.execute(
            """INSERT INTO tweet (user_id, text, date, localization)
            values (%s, %s, %s, %s);""", (user_id, status.text, status.created_at, str(status.coordinates) if status.coordinates != None else None)
        )
        conn.commit()
        cur.close()


    def get_user_id(self, conn, user):
        cur = conn.cursor()
        cur.execute("SELECT id FROM twitter_user WHERE username = '" + user.screen_name + "'")
        rows = cur.fetchall()
        if len(rows) == 0:
            cur.execute("""INSERT INTO twitter_user (username, followers_count, friends_count)
            VALUES (%s, %s, %s)""", (user.screen_name, user.followers_count, user.friends_count))
            conn.commit()
            cur.execute("SELECT id FROM twitter_user WHERE username = '" + user.screen_name + "'")
            return cur.fetchall()[0]
        else:
            return rows[0]
        cur.close()
        print rows
