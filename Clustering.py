from scipy.cluster.hierarchy import linkage

from util.Drawer import Drawer
from util.TextSimilarity import TextSimilarity
from util.TaskReader import TaskReader

task = TaskReader.read("text.txt")  # Чтение задания из файла
test = {"full": task.text, "nouns": task.education}
for text_type in test:
    similarity = TextSimilarity('french').get_cosine_similarity(test[text_type])  # Получение матрицы косинусной близости
    distances = 1 - similarity  # Получение матрицы расстояний
    linkage_matrix = linkage(distances, method='average', metric='cosine')  # Получение матрицы связей

    Drawer.draw_dendrogramm(linkage_matrix, range_start=244)
    Drawer.set_labels("Clustering - " + text_type)
    Drawer.save("Clustering_" + text_type + ".png")

