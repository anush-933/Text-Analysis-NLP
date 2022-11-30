from nltk.tokenize import sent_tokenize, word_tokenize
import re
from SyllableCount import syllables

def split(word):
    return list(word)

def comp_word_count_func(sentence):
    comp_word_c = 0
    beg_each_Sentence = re.findall(r"\.\s*(\w+)", sentence)
    capital_words = re.findall(r"\b[A-Z][a-z]+\b", sentence)
    words = word_tokenize(sentence)
    for word in words:
        if word not in capital_words and len(word) >= 3:  # all lower case words

            if syllables(word) >= 3 and len(split(word)) == 1:
                comp_word_c += 1

        if word in capital_words and word in beg_each_Sentence:  # beginning of each sentence is uppercase

            if syllables(word) >= 3:
                comp_word_c += 1
    return comp_word_c

def fog_index(sentence):
    words_count = len(word_tokenize(sentence))
    sent_count = len(sent_tokenize(sentence))
    complex_word_count = comp_word_count_func(sentence)
    fog_index_score = ((words_count / sent_count) + complex_word_count) * 0.4
    return round(fog_index_score,2)