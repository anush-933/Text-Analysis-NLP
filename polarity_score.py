from textblob import TextBlob

def polar_score(sentence):
    testimonial = TextBlob(sentence)
    return round(testimonial.sentiment.polarity, 2)