from util.TextSimilarity import TextSimilarity
from util.TaskReader import TaskReader

from gensim.corpora import Dictionary
from gensim.models.ldamodel import LdaModel

print("LDA Output: ")

first_num = 244

task = TaskReader.read("text.txt")
similarity = TextSimilarity('french')
doc_set = similarity.get_modified_text(task.text)
edu_set = similarity.get_modified_text(task.education)

dictionary = Dictionary([[x for x in i.split()] for i in edu_set])
for i in range(0, len(doc_set)):
    num = i + first_num
    corp = [x for x in doc_set[i].split()]
    corpus = [dictionary.doc2bow(corp)]
    ldamodel = LdaModel(corpus, num_topics=1, id2word=dictionary, passes=50)
    [print("Topic № " + str(num) + " : " + x[1]) for x in ldamodel.print_topics(num_topics=1, num_words=6)]