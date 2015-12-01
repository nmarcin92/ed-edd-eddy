from plotter.DataProcessor import DataProcessor
from plotter.Database import Database
from plotter.Plotter import Plotter

if __name__ == "__main__":
    database = Database()
    plotter = Plotter()
    processor = DataProcessor(database)

    # line, bar = processor.process_sentiment_for_category('Trump')
    # plotter.plot_line_and_bar('Trump', 'Sentiment', 'Total count', line, bar)
    data = processor.process_sentiment_for_all_categories(['democratic', 'republican'])
    legend = [d[0] for d in data]
    lines = [d[1] for d in data]
    bars = [d[2] for d in data]
    plotter.plot_many_lines_and_bars('Comparison', 'Sentiment', 'Total count', legend, lines, bars)
