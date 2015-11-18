from sentiment_analyzer.Database import Database
from sentiment_analyzer.SentimentAnalyzer import SentimentAnalyzer
from sentiment_analyzer.SentimentWord import SentimentWord

if __name__ == "__main__":
    database = Database()
    sentimentWords = SentimentWord()
    analyzer = SentimentAnalyzer(sentimentWords.get_words(), database)
    analyzer.find_sentiment_for_all()

