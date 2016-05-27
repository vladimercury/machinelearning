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

dendrogramm_clusters_nouns = [
    [256, 252, 291, 257, 286],
    [253, 250, 249],
    [262, 260, 261, 258, 251],
    [264, 247, 245, 265, 248],
    [267, 244, 254, 263, 255, 259],
    [275, 274, 276, 273, 272, 278, 277, 271, 270, 269, 268, 266],
    [282, 281, 280],
    [285, 284, 292, 283, 279],
    [289, 288, 290, 287, 246]
]

dendrogramm_clusters_full = [
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

expert_clusters = [
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

dendrogramm_clusters = {"full" : dendrogramm_clusters_full, "nouns" : dendrogramm_clusters_nouns}

for text_type in dendrogramm_clusters:
    prog_clusters = make_clusters(dendrogramm_clusters[text_type], 293-244, 244)
    exp_clusters = make_clusters(expert_clusters, 293-244, 244)
    print(text_type + " ================================")
    print(prog_clusters)
    print(exp_clusters)

    print()
    for i in range(1, len(expert_clusters) + 1):
        print(recall_precision(i, exp_clusters, prog_clusters))

    matrix = []
    vec = []
    for clust in expert_clusters:
        vec = []
        for dclust in dendrogramm_clusters[text_type]:
            val = 0
            for x in clust:
                if x in dclust:
                    val += 1
            vec.append(val)
        matrix.append(vec)

    print()
    # [print(vc) for vc in matrix]
    print()