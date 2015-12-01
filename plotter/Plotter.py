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
    def plot_many_lines(title, legend, data):
        fig, ax1 = plt.subplots()
        for plot in data:
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
    def plot_line_and_bar(title, line_label, bar_label, line, bar):
        fig, ax1 = plt.subplots()
        ax1.plot(line, linewidth=5)
        ax1.set_ylabel(line_label)

        ax2 = ax1.twinx()
        ax2.bar([b[0] for b in bar], [b[1] for b in bar])
        ax2.set_ylabel(bar_label)
        ax2.set_title(title)
        ax2.set_xlabel('Date from 01.11.2015 to 10.11.2015')
        plt.show()

    def plot_many_lines_and_bars(self, title, line_label, bar_label, legend, lines, bars):
        fig, ax1 = plt.subplots()
        for line in lines:
            ax1.plot(line, linewidth=5)
        ax1.set_ylabel(line_label)

        ax2 = ax1.twinx()
        color_cycle = ax2._get_lines.color_cycle
        for i in range(len(bars)):
            ax2.bar([self.count_x_val(b[0], i, len(legend)) for b in bars[i]], [b[1] for b in bars[i]], width=1.0/len(legend), align='edge', color=next(color_cycle))
        ax2.xaxis_date()
        ax2.autoscale(tight=True)
        ax2.set_ylabel(bar_label)
        ax2.set_title(title)
        ax2.legend(legend, loc='upper left')
        ax2.set_xlabel('Date from 01.11.2015 to 10.11.2015')
        plt.show()

    @staticmethod
    def count_x_val(x, i, length):
        s = -0.5
        s += i*(1.0/length)
        return float(x) + s
