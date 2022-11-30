from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def neg_score(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    negative_score = sentiment_dict['neg'] * 100
    return round(negative_score, 2)