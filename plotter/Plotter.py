import matplotlib.pyplot as plt


class Plotter:
    def __init__(self):
        pass

    @staticmethod
    def plot_line(title, data):
        fig, ax1 = plt.subplots()
        ax1.plot(data)
        ax1.set_title(title)
        ax1.set_xlabel('Date from 01.11.2015 to 10.11.2015')
        plt.show()

    @staticmethod
    def plot_many_lines(title, data):
        fig, ax1 = plt.subplots()
        legend = []
        for plot in data:
            legend.append(plot[0])
            ax1.plot(plot[1])
        ax1.legend(legend, loc='upper left')
        ax1.set_title(title)
        ax1.set_xlabel('Date from 01.11.2015 to 10.11.2015')
        plt.show()

    @staticmethod
    def plot_bar(title, x_val_list, y_val_list):
        fig, ax1 = plt.subplots()
        ax1.bar(x_val_list, y_val_list)
        ax1.set_title(title)
        ax1.set_xlabel('Date from 01.11.2015 to 10.11.2015')
        plt.show()

    @staticmethod
    def plot_line_and_bar(title, line, bar):
        fig, ax1 = plt.subplots()
        ax1.plot(line)
        ax1.set_title(title)
        ax1.set_xlabel('Date from 01.11.2015 to 10.11.2015')
        ax1.set_ylabel('Sentiment')

        ax2 = ax1.twinx()
        ax2.bar([b[0] for b in bar], [b[1] for b in bar])
        ax2.set_ylabel('Count')
        plt.show()
