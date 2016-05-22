from util.TaskReader import TaskReader
from util.Drawer import Drawer
from texttiling.FrenchTextTiling import FrenchTextTiling

import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

task = TaskReader.read("text.txt")
distances = 1 - FrenchTextTiling().get_cosine_similarity(task.text)
linkage_matrix = linkage(distances, method='average', metric='cosine')

Drawer.draw_dendrogramm(linkage_matrix, 'Clustering.png', 244, 'Clustering')