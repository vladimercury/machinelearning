import matplotlib.pyplot as plot

class Drawer:  # Класс для рисования диаграмм
    @staticmethod
    def draw_dendrogramm(linkage_matrix, range_start=1):
        # Нарисовать дендрограмму
        import matplotlib.pyplot as plot
        from scipy.cluster.hierarchy import dendrogram
        min = range_start
        max = range_start + len(linkage_matrix) + 1
        plot.figure(figsize=(20,20))
        dendrogram(linkage_matrix, orientation="right", labels=range(min,max))  # Создание дендрограммы

    @staticmethod
    def draw_bar_graph(hist_data, range_start=1, step=3, width=0.8, color='blue', drawxticks=True):
        # Нарисовать столбчатую диаграмму
        min = range_start
        max = range_start + len(hist_data)
        if drawxticks:
            plot.xticks(range(min, max, step))  # Подписи столбцов с определенным шагом
        plot.bar(range(min, max), hist_data, width=width, color=color)  # Создание диаграммы

    @staticmethod
    def draw_hline(length, height, start=1, color='black', linewidth=0.5):
        xval = range(start, start + length)
        yval = [height] * len(xval)
        plot.plot(xval, yval, color=color, linewidth=linewidth)

    @staticmethod
    def show():
        # Показ графика
        plot.show()

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
    def set_labels(title, xlabel='', ylabel=''):
        # Подпись диаграммы и осей
        plot.title(title)
        if xlabel != '':
            plot.xlabel(xlabel)
        if ylabel != '':
            plot.ylabel(ylabel)

