from plotter.DataProcessor import DataProcessor
from plotter.Database import Database
from plotter.Plotter import Plotter

if __name__ == "__main__":
    database = Database()
    plotter = Plotter()
    processor = DataProcessor(database)
    line, bar = processor.process_sentiment_for_category('Trump')
    plotter.plot_line_and_bar('Trump', line, bar)
