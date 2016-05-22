class Drawer:
    @staticmethod
    def draw_dendrogramm(linkage_matrix, output_file, range_start=1, plot_title="Dendrogramm"):
        import matplotlib.pyplot as plot
        from scipy.cluster.hierarchy import dendrogram
        plot.figure(figsize=(20, 20))
        plot.title(plot_title)
        labels=range(range_start, range_start + len(linkage_matrix) + 1)
        dendrogram(linkage_matrix, orientation="right", labels=labels)
        plot.tight_layout()
        plot.savefig(output_file, dpi=200)
        plot.close()

    @staticmethod
    def draw_histogramm(hist_data, output_file, range_start=1, plot_title="Histogramm"):
        import matplotlib.pyplot as plot
        from numpy import arange
        plot.title(plot_title)
        labels = arange(range_start, range_start + len(hist_data))
        plot.bar(labels, hist_data)
        plot.tight_layout()
        plot.savefig(output_file, dpi=200)
        plot.close()