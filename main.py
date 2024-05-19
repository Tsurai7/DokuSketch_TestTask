from PlotDrawer import PlotDrawer

def main():
    plot_drawer = PlotDrawer()
    json_file = "deviation.json"
    plot_paths = plot_drawer.draw_plots(json_file)

    for path in plot_paths:
        print(f"Plot saved at: {path}")

if __name__ == "__main__":
    main()