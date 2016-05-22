from util.TaskReader import TaskReader
from texttiling.FrenchTextTiling import FrenchTextTiling

import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

task = TaskReader.read("text.txt")
distances = 1 - FrenchTextTiling().get_cosine_similarity(task.text)
linkage_matrix = linkage(distances, method='average', metric='cosine')
plt.figure(figsize=(20, 20)) #set size
plt.title("Clustering")
dendrogram(linkage_matrix, orientation="right", labels=range(244, 293))

plt.tight_layout()
plt.savefig('Clustering.png', dpi=200)
plt.close()
