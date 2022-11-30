from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def pos_score(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    positive_score = sentiment_dict['pos'] * 100
    return round(positive_score, 2)