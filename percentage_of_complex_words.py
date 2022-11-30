from readability import Readability

def per_of_comp_words(sentence):
    text = sentence
    r = Readability(text)
    dc = r.dale_chall()
    return round(dc.score,2)