import spacy

nlp = spacy.load('en_core_web_sm')


def per_pronoun(sentence):
    personalP = []
    sen = nlp(sentence)
    for w in sen:
        if w.tag_ == 'PRP':
            personalP.append(w)

    return personalP
