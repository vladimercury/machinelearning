from util.TaskReader import TaskReader
from util.TextSimilarity import TextSimilarity


class SVM:
    def __init__(self, filename):
        task = TaskReader.read(filename)
        similarity = TextSimilarity('french')
        doc = [x.split() for x in similarity.get_modified_text(task.education)]
        spisok = [dict() for j in range(len(doc))]
        for j in range(len(doc)):
            for i in range(len(doc[j])):
                if spisok[j].get(doc[j][i]) is None:
                    spisok[j][doc[j][i]] = 1.0
                    for y in range(len(spisok)):
                        if spisok[y].get(doc[j][i]) is None:
                            spisok[y][doc[j][i]] = 0.0
                else:
                    spisok[j][doc[j][i]] += 1
                    for y in range(len(spisok)):
                        if spisok[y].get(doc[j][i]) is None:
                            spisok[y] = doc[j][i] = 0.0
        self.spisok = spisok
        self.c = [0] * len(spisok)
        self.cplus = []
        self.cminus = []
        self.igs = dict()
        self.dfi = dict()
        self.w = []
        self.b = 0.0

    def reset(self):
        self.c = [0] * len(self.spisok)
        self.cplus = []
        self.cminus = []
        self.igs = dict()
        self.dfi = dict()
        self.w = []
        self.b = 0.0

    def igplus(self, m):
        from math import log2
        a = sum([1 for x in range(len(self.cplus)) if self.spisok[self.cplus[x]-1].get(m) != 0])
        b = sum([1 for x in range(len(self.cminus)) if self.spisok[self.cminus[x]-1].get(m) != 0])
        c = sum([1 for x in range(len(self.cplus)) if self.spisok[self.cplus[x]-1].get(m) == 0])
        d = sum([1 for x in range(len(self.cminus)) if self.spisok[self.cminus[x]-1].get(m) == 0])
        q = len(self.cplus) + len(self.cminus)
        ans = 0.0
        if q != 0:
            if a != 0:
                ans += (a / q) * log2(q * a / ((a + b) * (a + c)))
            if c != 0:
                ans += (c / q) * log2(q * c / ((c + d) * (a + c)))
            if b != 0:
                ans += (b / q) * log2(q * b / ((a + b) * (b + d)))
            if d != 0:
                ans += (d / q) * log2(q * d / ((c + d) * (b + d)))
        self.igs[m] = ans

    def plus(self, args):
        self.cplus = [x + 1 for x in args]
        for i in range(len(self.cplus)):
            self.c[self.cplus[i] - 1] = 1

    def minus(self, args):
        self.cminus = [x + 1 for x in args]
        for i in range(len(self.cminus)):
            self.c[self.cminus[i] - 1] = -1

    def weight(self):
        from math import log2, sqrt
        keys = [x for x in self.igs.keys()]
        for i in range(len(self.spisok)):
            for j in range(len(keys)):
                if self.spisok[i].get(keys[j]) != 0:
                    self.igs[keys[j]] = self.igs.get(keys[j]) + 1
        for i in range(len(self.spisok)):
            w = 0.0
            for j in range(len(keys)):
                h = self.spisok[i].get(keys[j]) * log2(len(self.spisok) / self.igs.get(keys[j]))
                w += h * h
                self.spisok[i][keys[j]] = h
            w = sqrt(w)
            for j in range(len(keys)):
                self.spisok[i][keys[j]] = self.spisok[i].get(keys[j]) / w

    def aa(self):
        keys = [x for x in self.igs.keys()]
        a = [0.0] * len(self.spisok)
        suma = 0.0
        sw = [0.0] * len(self.spisok)
        sumsw = 0.0
        for i in range(len(self.spisok)):
            for j in range(len(keys)):
                if self.c[i] != 0:
                    sw[i] += self.spisok[i].get(keys[j])
                sumsw += sw[i]
        suma = 1 / sumsw
        sumcplus = sum([sw[self.cplus[i] - 1] for i in range(len(self.cplus))])
        sumcminus = sum([sw[self.cminus[i]-1] for i in range(len(self.cminus))])
        suma *= max(sumcplus, sumcminus)
        for i in range(len(self.cminus)):
            a[self.cminus[i] - 1] = (suma / sumcminus) * sw[self.cminus[i] - 1]
        for i in range(len(self.cplus)):
            a[self.cplus[i] - 1] = (suma / sumcplus) * sw[self.cplus[i] - 1]
        self.w = [0.0] * len(keys)
        for i in range(len(self.spisok)):
            for j in range(len(keys)):
                self.w[j] += a[i] * self.c[i] * self.spisok[i].get(keys[j])

    def bb(self):
        sum = 0.0
        keys = [x for x in self.igs.keys()]
        for i in range(len(self.spisok)):
            for j in range(len(self.spisok[i])):
                if self.c[i] != 0:
                    sum -= self.w[j] * self.spisok[i].get(keys[j])
        sum += len(self.cplus) - len(self.cminus)
        sum /= len(self.cplus) + len(self.cminus)
        self.b = sum

    def finish(self):
        keys = [x for x in self.igs.keys()]
        for i in range(len(self.spisok)):
            sm = self.b
            if self.c[i] == 0:
                sm += sum([self.w[j] * self.spisok[i].get(keys[j]) for j in range(len(keys))])
            self.c[i] = 1 if sm > 0 else -1


range_start = 244
themes = {
    "Фок":                  ([244, 251], [285, 286], [x for x in range(244, 254)]),
    "Бизань":               ([254, 261], [285, 286], [x for x in range(254, 263)]),
    "Блинд":                ([263, 265], [285], [x for x in range(263, 266)]),
    "Паруса между мачтами": ([266, 267, 270], [285], [x for x in range(266, 272)]),
    "Стаксели":             ([272, 277], [284], [x for x in range(272, 279)]),
    "Парусность судов":     ([280, 283], [287], [x for x in range(279, 284)]),
    "Снасти":               ([284], [281], [x for x in range(284, 286)]),
    "Блоки":                ([287, 291], [280], [x for x in range(286, 293)])
          }
themes = []
z = [x for x in range(244, 280)] + [x for x in range(283, 293)]
for i in range(0, len(z) - 1):
    for j in range(i + 1, len(z)):
        themes.append(([279, 280], [z[i], z[j]], [x for x in range(279, 284)]))
svm = SVM('text.txt')
for theme in range(len(themes)):
    svm.reset()
    svm.plus([x - range_start for x in themes[theme][0]])
    svm.minus([x - range_start for x in themes[theme][1]])
    keys = [x for x in svm.spisok[0].keys()]
    [svm.igplus(i) for i in keys]
    svm.weight()
    svm.aa()
    svm.bb()
    #out = open('svmout.txt', 'w')
    #for i in range(len(svm.spisok)):
    #keys1 = [x for x in svm.spisok[i].keys()]
    #out.write(''.join(["%s %f\n" % (j, svm.spisok[i].get(j)) for j in keys1 if svm.spisok[i].get(j) != 0.0]))
    #out.write(''.join(['='] * 50) + '\n')
    #out.write(''.join(["%s %f\n" % (keys[j], svm.w[j]) for j in range(len(keys)) if svm.w[j] != 0.0]))
    tsk = [x for x in svm.c]
    svm.finish()
    expert = [-1] * len(svm.c)
    for i in themes[theme][2]:
        expert[i - range_start] = 1
    diff = [expert[i] - svm.c[i] for i in range(len(expert))]
    diff_view = ['X' if diff[i] != 0 else ' ' for i in range(len(diff))]
    res = sum([1 if diff[i] != 0 else 0 for i in range(len(diff))])
    expert_diff = sum([1 if tsk[i] != 0 and tsk[i] != svm.c[i] else 0 for i in range(len(tsk))])
    if expert_diff < 3 and res < 5:
        print(''.join(["="] * 30) + " " + str(theme) + " " + ''.join(["="] * 30))
        print(''.join(["%3d " % i for i in range(range_start, range_start + len(svm.c))]))
        print(''.join(["%3d " % tsk[i] for i in range(len(tsk))]))
        print(''.join(["%3d " % svm.c[i] for i in range(len(svm.c))]))
        print(''.join(["%3d " % expert[i] for i in range(len(expert))]))
        print(''.join(["%3s " % diff_view[i] for i in range(len(diff_view))]))
    else:
        print(str(theme) + "/" + str(len(themes)))
