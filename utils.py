from random import randint
from Classes import BasicWord


def load_random_word(words):
    len_words = len(words)
    random_int = randint(0, len_words-1)
    random_word = words[random_int]
    return BasicWord(random_word.get("word"), random_word.get("subwords"))