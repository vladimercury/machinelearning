from util.TaskReader import TaskReader
from util.Drawer import Drawer
from texttiling.FrenchTextTiling import FrenchTextTiling

from scipy.cluster.hierarchy import linkage

task = TaskReader.read("text.txt")  # Чтение задания из файла

# Segmentation
similarity = FrenchTextTiling().get_cosine_similarity(task.text)  # Получение матрицы косинусной близости
cosines = [similarity[i][i+1] for i in range(0, len(similarity) - 1)]  # Получение массива косинусных близостей для соседних абзацев
Drawer.draw_bar_graph(cosines, "Segmentation.png", 244, "Segmentation")  # Создание диаграммы

# Clustering
distances = 1 - similarity  # Получение матрицы расстояний
linkage_matrix = linkage(distances, method='average', metric='cosine')  # Получение матрицы связей
Drawer.draw_dendrogramm(linkage_matrix, 'Clustering.png', 244, 'Clustering')  # Создание дендрограммы