import psycopg2

conn = psycopg2.connect("dbname=twitter user=postgres password=postgres")
cur = conn.cursor()
cur.execute("SELECT id,word FROM sentiment")
keywords = [(k[0],k[1]) for k in cur.fetchall()]

cur.execute("SELECT id, text FROM tweet")
tweets = [(k[0],k[1]) for k in cur.fetchall()]

i=0
for t in tweets:
    for k in keywords:
        if k[1] in t[1]:
            cur.execute(
                """INSERT INTO sentiment_tweet (sentiment, tweet)
                values (%s, %s);""", (k[0], t[0])
            )
    i += 1
    if i%100==0:
        conn.commit()
        print float(i) / len(tweets)
