class SentimentAnalyzer:
    def __init__(self, sentiment_words, database):
        self.sentiment_words = sentiment_words
        self.database = database

    def find_sentiment(self, text):
        splitted_text = text.lower().split()
        underline_text = "_".join(splitted_text)
        word_count = 0
        positive_sum = 0
        negative_sum = 0
        for sw in self.sentiment_words:
            if "_" not in sw[0]:
                for word in splitted_text:
                    if sw[0] == word:
                        word_count += 1
                        positive_sum += sw[1]
                        negative_sum += sw[2]
            else:
                if sw[0] in underline_text:
                    word_count += 1
                    positive_sum += sw[1]
                    negative_sum += sw[2]
        if word_count == 0:
            return self.specify_sentiment(0)
        score = (positive_sum - negative_sum) / word_count
        return self.specify_sentiment(score)

    @staticmethod
    def specify_sentiment(score):
        if score < -0.5:
            return 'NEGATIVE'
        elif score < -0.1:
            return 'SEMI_NEGATIVE'
        elif score < 0.01:
            return 'NEUTRAL'
        elif score < 0.5:
            return 'SEMI POSITIVE'
        elif score <= 1.0:
            return 'POSITIVE'

    def find_sentiment_for_all(self):
        tweets = self.database.find_tweets()
        for tweet in tweets:
            sentiment_score = self.find_sentiment(tweet[1])
            self.database.save_sentiment(tweet[0], sentiment_score)


