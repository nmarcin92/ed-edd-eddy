import sys
import psycopg2

conn = psycopg2.connect("dbname=twitter user=postgres password=postgres")
cur = conn.cursor()

file = open('sentiment.txt', 'r')
sentiments = []
for line in file:
    sent = []
    splitted = line.split('\t')
    sent.append(splitted[4][0:splitted[4].find('#')])
    sent.append(splitted[2])
    sent.append(splitted[3])
    sentiments.append(sent)

for s in sentiments:
    cur.execute(
        """INSERT INTO sentiment (word, positive_score, negative_score)
        values (%s, %s, %s);""", (s[0], s[1], s[2])
    )
conn.commit()
