from datetime import datetime

DENSITY = 10
START_DATE = datetime(2015, 11, 01)
END_DATE = datetime(2015, 11, 10)
INTERVAL = (END_DATE - START_DATE).total_seconds() / DENSITY


class DataProcessor:
    def __init__(self, database):
        self.db = database

    @staticmethod
    def get_sentiments_value(sent):
        if sent == 'NEGATIVE':
            return -1.0
        elif sent == 'SEMI_NEGATIVE':
            return -0.5
        elif sent == 'POSITIVE':
            return 1.0
        elif sent == 'SEMI POSITIVE':
            return 0.5
        else:
            return 0.0

    @staticmethod
    def find_time_span(date):
        return min(int(((date - START_DATE).total_seconds()) / INTERVAL), DENSITY - 1)

    def process_sentiment_for_category(self, category):
        tweets = sorted(self.db.find_tweets_by_category(category, START_DATE, END_DATE), key=lambda tweet: tweet[1])
        sentiments = [[0.0, 0.0] for i in range(DENSITY)]
        for t in tweets:
            time_span = self.find_time_span(t[1])
            data = sentiments[time_span]
            data[0] += self.get_sentiments_value(t[2])
            data[1] += 1
        return [(float(data[0]) / data[1]) if data[1] > 0 else 0.0 for data in sentiments], [(i, sentiments[i][1]) for i in range(DENSITY)]

    def process_sentiment_for_all_categories(self, categories):
        result = []
        for category in categories:
            line, bar = self.process_sentiment_for_category(category)
            result.append((category, line, bar))
        return result


