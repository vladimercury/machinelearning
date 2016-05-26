from scipy.cluster.hierarchy import linkage

from util.Drawer import Drawer
from util.TextSimilarity import TextSimilarity
from util.TaskReader import TaskReader

task = TaskReader.read("text.txt")  # Чтение задания из файла
similarity = TextSimilarity('french').get_cosine_similarity(task.text)  # Получение матрицы косинусной близости
distances = 1 - similarity  # Получение матрицы расстояний
linkage_matrix = linkage(distances, method='average', metric='cosine')  # Получение матрицы связей

Drawer.draw_dendrogramm(linkage_matrix, range_start=244)
Drawer.set_labels("Clustering")
Drawer.save("Clustering.png")

