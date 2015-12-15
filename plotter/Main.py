from plotter.DataProcessor import DataProcessor
from plotter.Database import Database
from plotter.Plotter import Plotter

if __name__ == "__main__":
    database = Database()
    plotter = Plotter()
    processor = DataProcessor(database)

    for category in database.find_all_categories():
        line, bar = processor.process_sentiment_for_category(category)
        plotter.save_line_and_bar(category, 'Sentiment', 'Total count', line, bar)

    comparisons = [('democratic', 'republican'), ('Trump', 'Clinton')]
    for comparison in comparisons:
        data = processor.process_sentiment_for_all_categories(comparison)
        legend = [d[0] for d in data]
        lines = [d[1] for d in data]
        bars = [d[2] for d in data]
        plotter.save_many_lines_and_bars('{0} vs {1}'.format(comparison[0], comparison[1]), 'Sentiment', 'Total count', legend, lines, bars)
