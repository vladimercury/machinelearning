from util.TextSimilarity import TextSimilarity
from util.TaskReader import TaskReader

from gensim.corpora import Dictionary
from gensim.models.ldamodel import LdaModel

print("LDA Output: ")

task = TaskReader.read("text.txt")
similarity = TextSimilarity('french')
text = similarity.get_modified_text(task.text)
edu = similarity.get_modified_text(task.education)
for i in range(0, len(text)):
    num = i + 244
    corp = [x for x in text[i].split()]
    dict = [x for x in edu[i].split()]
    dictionary = Dictionary([dict])
    corpus = [dictionary.doc2bow(corp)]
    ldamodel = LdaModel(corpus, num_topics=1, id2word=dictionary, passes=20)
    [print(str(num) + " : " + x[1]) for x in ldamodel.print_topics(num_topics=1, num_words=6)]
