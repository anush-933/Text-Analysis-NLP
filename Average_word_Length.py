from nltk.tokenize import word_tokenize


def avg_word_length(sentence):
    len_of_words = 0
    tot_words = 0
    words = word_tokenize(sentence)
    for x in words:
        len_of_words += len(x)
        tot_words += 1
    avg_w_length = len_of_words / tot_words
    return round(avg_w_length, 2)
