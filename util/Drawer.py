import matplotlib.pyplot as plot

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
    def draw_bar_graph(hist_data, range_start=1, step=3, width=0.8, color='blue', drawxticks=True):
        # Нарисовать столбчатую диаграмму
        min = range_start
        max = range_start + len(hist_data)
        plot.bar(range(min, max), hist_data, width=width, color=color)  # Создание диаграммы
        if drawxticks:
            plot.xticks(range(min, max, step))  # Подписи столбцов с определенным шагом

    @staticmethod
    def draw_hline(length, height, start=1, color='black', linewidth=0.5):
        xval = range(start, start + length)
        yval = [height] * len(xval)
        plot.plot(xval, yval, color=color, linewidth=linewidth)

    @staticmethod
    def reset():
        # Очистка графика
        plot.close()

    @staticmethod
    def save(file_name, dpi=200):
        # Сохранение в файл
        plot.tight_layout()
        plot.savefig(file_name, dpi=dpi)

    @staticmethod
    def set_labels(title, xlabel, ylabel):
        # Подпись диаграммы и осей
        plot.title(title)
        plot.xlabel(xlabel)
        plot.ylabel(ylabel)

