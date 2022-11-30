from textblob import TextBlob


def subject_score(sentence):
    testimonial = TextBlob(sentence)
    return round(testimonial.sentiment.subjectivity, 2)
