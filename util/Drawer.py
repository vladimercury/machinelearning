class Drawer:
    @staticmethod
    def draw_dendrogramm(linkage_matrix, output_file, range_start=1, plot_title="Dendrogramm"):
        import matplotlib.pyplot as plot
        from scipy.cluster.hierarchy import linkage, dendrogram
        plot.figure(figsize=(20, 20))
        plot.title(plot_title)
        dendrogram(linkage_matrix, orientation="right", labels=range(range_start, range_start + len(linkage_matrix)+1))
        plot.tight_layout()
        plot.savefig(output_file, dpi=200)
        plot.close()