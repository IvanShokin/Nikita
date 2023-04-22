class BasicWord:
    def __init__(self, original_word, subwords):
        self.original_word = original_word
        self.subwords = subwords

    def is_in_subwords(self, input_word):
        return input_word in self.subwords

    def count_word(self):
        return len(self.subwords)

    def __repr__(self):
        return self.original_word

    def len_word(self):
        return len(self.original_word)

class Player:
    def __init__(self, name):
        self.name = name
        self.used_words = []

    def get_len_used_words(self):
        return len(self.used_words)

    def add_word(self, word):
        self.used_words.append(word)

    def is_in_used_words(self, word):
        return word in self.used_words

    def __repr__(self):
        return self.name