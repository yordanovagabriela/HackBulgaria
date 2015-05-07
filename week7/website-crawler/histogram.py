class Histogram:
    def __init__(self):
        self.items = {}

    def add(self, word):
        if word not in self.items:
            self.items[word] = 1
        else:
            self.items[word] += 1

    def count(self, word):
        return self.items[word]

    def get_dict(self):
        return self.items
