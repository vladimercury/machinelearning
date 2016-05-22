class FrenchTextTiling:
    def __init__(self):
        from nltk.corpus import stopwords
        from nltk.stem.snowball import SnowballStemmer
        from sklearn.feature_extraction.text import TfidfVectorizer
        # Инициализация
        self.lang = 'french'
        self.words = stopwords.words(self.lang) + ['fig', 'a', 'f']
        self.stemmer = SnowballStemmer(self.lang)
        self.vectorizer = TfidfVectorizer(min_df=0.1)

    def _get_stemmed_tokens(self, paragraph):
        from string import punctuation, digits
        from nltk import word_tokenize
        # Возвращает слова из абзаца в нижнем регистре, без пунктуации, чисел и стоп-слов
        lower_case = paragraph.lower()
        no_punctuation = lower_case.translate(str.maketrans(punctuation, " " * len(punctuation)))
        no_digits = no_punctuation.translate(str.maketrans(digits, " " * len(digits)))
        tokens = word_tokenize(no_digits)
        return [self.stemmer.stem(x) for x in tokens if x not in self.words]

    def _get_modified_text(self, text):
        # Возвращает модифицированные абзацы
        modified_text = []
        for line in text:
            tokens = self._get_stemmed_tokens(line)
            new_line = ""
            for token in tokens:
                new_line += token + " "
            modified_text.append(new_line)
        return modified_text

    def get_cosine_similarity(self, text):
        from sklearn.metrics.pairwise import cosine_similarity
        # Возвращает матрицу связей
        modified_text = self._get_modified_text(text)
        matrix = self.vectorizer.fit_transform(modified_text)
        return cosine_similarity(matrix)