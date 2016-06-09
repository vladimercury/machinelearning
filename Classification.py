from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC, SVC
from sklearn import metrics
from util.TaskReader import TaskReader
from util.TextSimilarity import TextSimilarity
from util.Drawer import Drawer


class F:
    def __init__(self, data=None, target=None, target_names=None):
        self.data = data
        self.target = target
        self.target_names = target_names


def cut(data, target, indexes, range_start=1):
    new_data = []
    new_target = []
    for i in indexes:
        new_data.append(data[i-range_start])
        new_target.append(target[i-range_start])
    return new_data, new_target


similarity = TextSimilarity('french')
task = TaskReader.read('text.txt')
text = similarity.get_modified_text(task.text)
f = F()
f.data = text
f.target = target = [0] * 10 + [1] * 9 + [2] * 3 + [3] * 6 + [4] * 7 + [5] * 5 + [6] * 2 + [7] * 7
education_cut = [244, 247, 251, 254, 258, 261, 263, 265, 266, 267, 270, 272, 275, 277, 280, 283, 285, 287, 290]
f.data, f.target = cut(f.data, f.target, education_cut, range_start=244)
f.target_names = ["Фок", "Бизань", "Блинд", "Паруса между мачтами", "Стаксели", "Парусность судов", "Снасти", "Блоки"]

text_clf = Pipeline([('vect', TfidfVectorizer()), ('tfidf', TfidfTransformer()), ('clf', SVC(kernel='linear'))])
text_clf.fit(f.data, f.target)
predicted = text_clf.predict(text)

tmp = [-1] * len(target)
for i in education_cut:
    tmp[i - 244] = target[i - 244]

print("edu    : " + ' '.join([' ' if x == -1 else str(x + 1) for x in tmp]))
print("expert : " + ' '.join([str(x + 1) for x in target]))
print("svm    : " + ' '.join([str(x + 1) for x in predicted]))
print(metrics.classification_report(target, predicted, target_names=f.target_names))

Drawer.draw_bar_graph([x+1 for x in predicted], range_start=244, step=3)
Drawer.set_labels("Classification using SVM", "Documents", "Classes")
Drawer.save("Classification_svm.png")

Drawer.reset()
Drawer.draw_bar_graph([x+1 for x in target], range_start=244, step=3)
Drawer.set_labels("Classification by expert", "Documents", "Classes")
Drawer.save("Classification_expert.png")