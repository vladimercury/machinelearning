from util.TaskReader import TaskReader
from util.Drawer import Drawer
from texttiling.FrenchTextTiling import FrenchTextTiling

from scipy.cluster.hierarchy import linkage

task = TaskReader.read("text.txt")

# Segmentation
similarity = FrenchTextTiling().get_cosine_similarity(task.text)
cosines = [similarity[i][i+1] for i in range(0, len(similarity) - 1)]
Drawer.draw_histogramm(cosines, "Segmentation.png", 244, "Segmentation")

# Clustering
distances = 1 - similarity
linkage_matrix = linkage(distances, method='average', metric='cosine')
#Drawer.draw_dendrogramm(linkage_matrix, 'Clustering.png', 244, 'Clustering')