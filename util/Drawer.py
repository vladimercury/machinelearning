class Drawer:  # Класс для рисования диаграмм
    @staticmethod
    def draw_dendrogramm(linkage_matrix, output_file, range_start=1, plot_title="Dendrogramm"):
        # Нарисовать дендрограмму
        import matplotlib.pyplot as plot
        from scipy.cluster.hierarchy import dendrogram
        plot.figure(figsize=(20, 20))
        plot.title(plot_title)  # Заголовок
        labels=range(range_start, range_start + len(linkage_matrix) + 1)  # Создание подписей столбцов
        dendrogram(linkage_matrix, orientation="right", labels=labels)  # Создание дендрограммы
        plot.tight_layout()  # Обрезаются белые поля
        plot.savefig(output_file, dpi=200)  # Запись в файл
        plot.close()

    @staticmethod
    def draw_bar_graph(hist_data, output_file, range_start=1, plot_title="Bar graph"):
        # Нарисовать столбчатую диаграмму
        import matplotlib.pyplot as plot
        plot.title(plot_title)  # Заголовок
        labels = range(range_start, range_start + len(hist_data))  # Создание подписей столбцов
        plot.bar(labels, hist_data)  # Создание диаграммы
        plot.tight_layout()  # Обрезаются белые поля
        plot.savefig(output_file, dpi=200)  # Запись в файл
        plot.close()
