class TextSimilarity:  # Класс для определения косинусной близости абзацев текста
    def __init__(self, lang):
        # Инициализация
        from nltk.corpus import stopwords
        from nltk.stem.snowball import SnowballStemmer
        from sklearn.feature_extraction.text import TfidfVectorizer
        self.lang = lang  # Язык
        self.words = stopwords.words(self.lang) # Стоп-слова (союзы, предлоги)
        self.stemmer = SnowballStemmer(self.lang)  # Класс, выделяющий основные части слов
        self.vectorizer = TfidfVectorizer(min_df=0.1)  # Класс для построения TF-IDF матрицы

    def _get_modified_tokens(self, paragraph):
        # Возвращает слова из абзаца в нижнем регистре, без пунктуации, чисел и стоп-слов
        from string import punctuation, digits
        from nltk import word_tokenize
        lower_case = paragraph.lower()  # Преобразование в нижний регистр
        no_punctuation = lower_case.translate(str.maketrans(punctuation, " " * len(punctuation)))  # Удаление знаков
        no_digits = no_punctuation.translate(str.maketrans(digits, " " * len(digits)))  # Удаление цифр
        tokens = word_tokenize(no_digits)  # Разбиение на слова
        result = [self.stemmer.stem(x) for x in tokens if x not in self.words]  # Выделение основных частей слов
        return result

    def get_modified_text(self, text):
        # Возвращает модифицированный текст
        modified_text = []
        for line in text:
            tokens = self._get_modified_tokens(line)  # Получение модифицированных слов
            new_line = ""
            for token in tokens:
                new_line += token + " "  # Сборка массива слов обратно в строку
            modified_text.append(new_line)  # Добавление очередной строки в массив
        return modified_text

    def get_cosine_similarity(self, text):
        # Возвращает матрицу косинусной близости
        from sklearn.metrics.pairwise import cosine_similarity
        modified_text = self.get_modified_text(text)  # Получение модифицированного текста
        matrix = self.vectorizer.fit_transform(modified_text)  # Получение TF-IDF матрицы
        cosine = cosine_similarity(matrix)  # Получение матрицы косинусной близости
        return cosine
