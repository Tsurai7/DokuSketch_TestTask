import os
import pandas as pd
import matplotlib.pyplot as plt


class PlotDrawer:
    def __init__(self, plot_dir="plots"):
        self.plot_dir = plot_dir
        if not os.path.exists(self.plot_dir):
            os.makedirs(self.plot_dir)

    def draw_plots(self, json_file):
        df = pd.read_json(json_file)
        plot_paths = []

        columns_to_plot = df.columns[2:]

        for col in columns_to_plot:
            plt.figure()
            df.plot(x='name', y=col, kind='bar', legend=False)
            plt.title(f'Room {col.capitalize()} Deviations')
            plt.ylabel('Degrees')
            plt.xlabel('Room Name')

            plot_path = os.path.join(self.plot_dir, f'{col}.png')
            plt.savefig(plot_path)
            plot_paths.append(plot_path)
            plt.close()

        return plot_paths