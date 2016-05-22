class TaskContainer:
    def __init__(self, text, education):
        self.text = text
        self.education = education

    def get_text(self):
        return self.text

    def get_education_set(self):
        return self.education


class TaskReader:
    @staticmethod
    def read(filename):
        from codecs import open
        file = open(filename, 'r', 'UTF-8')
        lines = file.read().splitlines()
        text = [lines[i] for i in range(0, len(lines)) if i % 2 == 0]
        education = [lines[i] for i in range(0, len(lines)) if i % 2 != 0]
        return TaskContainer(text, education)
