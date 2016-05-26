from numpy import arange

from util.Drawer import Drawer
from util.TextSimilarity import TextSimilarity
from util.TaskReader import TaskReader


def recall_precision(cos, bound_val, max_val, expert):
    bounds = []
    for x in cos:
        if x < bound_val:
            bounds.append(max_val)
        else:
            bounds.append(0)
    tp = fp = tn = fn = 0
    for i in range(0, len(bounds)):
        if bounds[i] == expert[i] and bounds[i] != 0:
            tp += 1
        elif bounds[i] == expert[i] and bounds[i] == 0:
            tn += 1
        elif bounds[i] != expert[i] and bounds[i] != 0:
            fp += 1
        elif bounds[i] != expert[i] and bounds[i] == 0:
            fn += 1
    recall = tp / (tp + fn)
    precision = tp / (tp + fp)
    F = 2 * precision * recall / (precision + recall)
    return F, recall, precision, tp, fn, fp, tn, bounds


task = TaskReader.read("text.txt")
similarity = TextSimilarity('french').get_cosine_similarity(task.text)
cosines = [similarity[i][i+1] for i in range(0, len(similarity) - 1)]

expert_bounds = []
expert_bound_value = [250, 253, 258, 262, 265, 266, 269, 271, 278, 283, 285, 291]
for x in range(244, 244 + len(cosines)):
    if x in expert_bound_value:
        expert_bounds.append(1)
    else:
        expert_bounds.append(0)

max_F = 0.0
max_bound = 0.0

for bound_value in arange(0.1, max(cosines), 0.01):
    F, recall, precision, tp, fn, fp, tn, bounds = recall_precision(cosines, bound_value, 1, expert_bounds)
    if F > max_F:
        max_F = F
        max_bound = bound_value

F, recall, precision, tp, fn, fp, tn, bounds = recall_precision(cosines, max_bound, 1, expert_bounds)

print("z = " + str(max_bound))
print("F = " + str(F))
print("R = " + str(recall) + ", P = " + str(precision))
print("tp = " + str(tp) + ", fp = " + str(fp) + ", tn = " + str(tn) + ", fn = " + str(fn))
print("expert bounds : " + str(expert_bounds))
print("program bounds: " + str(bounds))

Drawer.draw_bar_graph(cosines, range_start=244, step=3)
Drawer.draw_bar_graph(bounds, range_start=244, drawxticks=False, width=0.1, color='black')
Drawer.draw_hline(len(cosines), max_bound, start=244, color='r', linewidth=2)
Drawer.set_labels("Segmentation with program bounds", "Documents", "Cos(fi)")
Drawer.save("Segmentation_prog.png")

Drawer.reset()
Drawer.draw_bar_graph(cosines, range_start=244, step=3)
Drawer.draw_bar_graph(expert_bounds, range_start=244, drawxticks=False, width=0.1, color='black')
Drawer.set_labels("Segmentation with expert bounds", "Documents", "Cos(fi)")
Drawer.save("Segmentation_expert.png")