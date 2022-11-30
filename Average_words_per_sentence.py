from nltk.tokenize import word_tokenize


def avg_words_per_sentence(sentence):
    words = word_tokenize(sentence)
    sentences = [[]]
    ends = set(".?!")
    for w in words:
        if w in ends:
            sentences.append([])
        else:
            sentences[-1].append(w)
    if sentences[0]:
        if not sentences[-1]: sentences.pop()
        avg = sum(len(s) for s in sentences) / len(sentences)

    return round(avg,2)