from nltk.tokenize import sent_tokenize, word_tokenize


def avg_sent_len(sentence):
    sent = sent_tokenize(sentence)
    words = word_tokenize(sentence)
    num_of_words = len(words)
    num_of_sent = len(sent)
    avg_sent_length = float(num_of_words / num_of_sent)
    return round(avg_sent_length, 2)
