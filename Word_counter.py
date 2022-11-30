from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string


stop_words = set(stopwords.words('english'))
s =  set(string.punctuation)

def word_count(sentence):
    word_tokens = word_tokenize(sentence)
    stop_words = set(stopwords.words('english'))
    filtered_words = []

    for w in word_tokens:
        if w not in stop_words:
            if w not in s:
                filtered_words.append(w)

    # print(num_of_words)
    total_words = len(filtered_words)
    return(total_words)
