from datetime import datetime

import matplotlib.pyplot as plt

from plotter.Database import Database

DENSITY = 100


def get_sentiments_value(sent):
    if sent == 'NEGATIVE':
        return -1.0
    elif sent == 'SEMI_NEGATIVE':
        return -0.5
    elif sent == 'NEUTRAL':
        return 0.0
    elif sent == 'POSITIVE':
        return 0.5
    else:
        return 1.0


def plot_sentiment_changes(category, start_date, end_date):
    database = Database()
    tweets = sorted(database.find_tweets_by_category(category, start_date, end_date), key=lambda t: t[1])
    min_date = tweets[0][1]
    max_date = tweets[len(tweets) - 1][1]
    interval = (max_date - min_date).total_seconds() / DENSITY
    sentiments = [[0.0, 0.0] for i in range(DENSITY)]
    for t in tweets:
        timespan = min(int(((t[1] - min_date).total_seconds()) / interval), DENSITY - 1)
        coords = sentiments[timespan]
        sent = get_sentiments_value(t[2])
        if sent > 0:
            coords[0] += sent
        coords[1] += int(abs(sent))

    plt.plot([(float(coords[0]) / coords[1]) if coords[1] != 0 else 0.5 for coords in sentiments])
    plt.show()


plot_sentiment_changes('republican', datetime(2015, 11, 01), datetime(2015, 11, 15))
