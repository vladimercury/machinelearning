def make_clusters(clusters, length, range_start=1):
    res = [0] * length
    for i in range(0, len(res)):
        for j in range(0, len(clusters)):
            if res[i] != 0:
                break
            for document in clusters[j]:
                if document == range_start + i:
                    res[i] = j + 1
                    break
    return res


def recall_precision(val, expert, prog):
    tp = fp = tn = fn = 0
    for i in range(0, len(expert)):
        if prog[i] == val and expert[i] == val:
            tp += 1
        elif prog[i] != val and expert[i] != val:
            tn += 1
        elif prog[i] == val and expert[i] != val:
            fp += 1
        elif prog[i] != val and expert[i] == val:
            fn += 1
    recall = precision = F = 0
    if tp != 0:
        recall = tp / (tp + fn)
        precision = tp / (tp + fp)
        F = 2 * precision * recall / (precision + recall)
    return F, recall, precision, tp, fn, fp, tn


dendrogramm_clusters6 = [
    [265, 258, 264, 247, 245, 248, 259],
    [272, 266, 282, 280, 281, 279, 291],
    [256, 252, 262, 260, 251, 261, 257, 278, 277, 275, 274, 276, 273, 271, 270, 268, 269],
    [263, 244, 254, 267, 255],
    [253, 250, 249],
    [288, 246, 289, 287, 290, 284, 283, 292, 286, 285]
]

expert_clusters6 = [
    [245, 246, 247, 255, 256, 257, 258, 264, 291],
    [254, 244, 266, 272, 279, 280, 281, 282, 282, 283],
    [248, 249, 250, 251, 252, 253, 261, 265, 270, 271, 273, 274, 275, 276, 277, 278],
    [259, 260, 262, 263, 267, 268, 269],
    [284, 285],
    [286, 287, 288, 289, 290]
]

dendrogramm_clusters9 = [
    [256, 252],
    [253, 250, 249],
    [262, 260, 251, 261, 257],
    [265, 258, 264, 247, 245, 248, 259],
    [263, 244, 254, 267, 255],
    [278, 277, 275, 274, 276, 273, 271, 270, 268, 269],
    [272, 266, 282, 280, 281, 279, 291],
    [284, 283, 292, 286, 285],
    [288, 246, 289, 287, 290]
]

expert_clusters9 = [
    [245, 246, 247, 255, 256, 257, 258, 264, 268, 260, 291],
    [254, 244, 248, 249, 250, 251, 252, 253],
    [259, 262, 261],
    [263, 265],
    [266, 267, 269, 270, 271],
    [272, 273, 274, 275, 276, 277, 278],
    [279, 283, 280, 281, 282],
    [284, 285],
    [286, 287, 288, 289, 290]
]

dendrogramm_clusters = dendrogramm_clusters9
expert_clusters = expert_clusters9

prog_clusters = make_clusters(dendrogramm_clusters, 293-244, 244)
exp_clusters = make_clusters(expert_clusters, 293-244, 244)
print(prog_clusters)
print(exp_clusters)

print()
for i in range(1, len(expert_clusters) + 1):
    print(recall_precision(i, exp_clusters, prog_clusters))

matrix = []
vec = []
for clust in expert_clusters:
    vec = []
    for dclust in dendrogramm_clusters:
        val = 0
        for x in clust:
            if x in dclust:
                val += 1
        vec.append(val)
    matrix.append(vec)

print()
[print(vc) for vc in matrix]