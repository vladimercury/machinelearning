class TaskContainer:  # Класс для хранения текста и его обучающего множества
    def __init__(self, text, education):
        self.text = text
        self.education = education

    def get_text(self):
        return self.text

    def get_education_set(self):
        return self.education


class TaskReader:  # Класс для разделения текста и обучающего множества при чтении из файла
    @staticmethod
    def read(filename):
        from codecs import open
        file = open(filename, 'r', 'UTF-8')
        lines = file.read().splitlines()  # Все строки файла
        text = [lines[i] for i in range(0, len(lines)) if i % 2 == 0]  # Сам текст
        education = [lines[i] for i in range(0, len(lines)) if i % 2 != 0]  # Обучающее множество
        return TaskContainer(text, education)
