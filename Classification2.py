from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC, SVC
from sklearn import metrics
from util.TaskReader import TaskReader
from util.TextSimilarity import TextSimilarity


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
edu = similarity.get_modified_text(task.education)
f = F()
f.data = text
f.target = target = [0] * 10 + [1] * 9 + [2] * 3 + [3] * 6 + [4] * 7 + [5] * 5 + [6] * 2 + [7] * 7
f.data, f.target = cut(f.data, f.target, [244, 246, 251, 254, 261, 263, 265, 266, 267, 270, 272, 277, 280, 283, 284, 287, 291], range_start=244)
f.target_names = ["Фок", "Бизань", "Блинд", "Паруса между мачтами", "Стаксели", "Парусность судов", "Снасти", "Блоки"]

text_clf = Pipeline([('vect', TfidfVectorizer()), ('tfidf', TfidfTransformer()), ('clf', SVC(kernel='linear'))])
text_clf.fit(f.data, f.target)
predicted = text_clf.predict(text)

print("expert : " + ' '.join([str(x) for x in target]))
print("svm    : " + ' '.join([str(x) for x in predicted]))
print(metrics.classification_report(target, predicted, target_names=f.target_names))