from datetime import datetime
from plotter.DataProcessor import DataProcessor
from plotter.Database import Database
from plotter.Plotter import Plotter

if __name__ == "__main__":
    database = Database()
    plotter = Plotter()
    processor = DataProcessor(database)

    # plotter.save_bar('All tweets count', processor.process_count())
    #
    # for category in database.find_all_categories():
    #     line, bar = processor.process_sentiment_for_category(category)
    #     plotter.save_line_and_bar(category, 'Sentiment', 'Total count', line, bar)
    #
    # comparisons = [('democratic', 'republican'), ('Trump', 'Clinton')]
    # for comparison in comparisons:
    #     data = processor.process_sentiment_for_categories(comparison)
    #     legend = [d[0] for d in data]
    #     lines = [d[1] for d in data]
    #     bars = [d[2] for d in data]
    #     plotter.save_many_lines_and_bars('{0} vs {1}'.format(comparison[0], comparison[1]), 'Sentiment', 'Total count', legend, lines, bars)

    START_DATE = datetime(2015, 10, 01)
    END_DATE = datetime(2015, 11, 11)
    users = ['realDonaldTrump', 'HillaryClinton', 'JebBush', 'tedcruz', 'BernieSanders']
    for user in users:
        line, bar = processor.process_sentiment_for_user(user, START_DATE, END_DATE)
        plotter.save_line_and_bar(user, 'Sentiment', 'Total count', line, bar)