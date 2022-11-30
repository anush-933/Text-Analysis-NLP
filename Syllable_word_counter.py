from nltk.tokenize import word_tokenize
from SyllableCount import syllables


def syy_per_word(sentence):
    sy_for_a_word = []
    words = word_tokenize(sentence)
    for w in words:
        sy_for_a_word.append(syllables(w))
    no_of_sy = sum(sy_for_a_word)
    tot_words = len(words)
    syllable_per_word = no_of_sy / tot_words
    return round(syllable_per_word, 2)
