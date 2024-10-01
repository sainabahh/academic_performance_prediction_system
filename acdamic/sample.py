import requests
import nltk
def sent(k):

    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    nltk.download('vader_lexicon')

    pstv = 0
    ngtv = 0
    ntl = 0
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(k)
    print("outttt",ss)
    a = float(ss['pos'])
    b = float(ss['neg'])
    c = float(ss['neu'])
    emo="Neutral"
    rating = 2.5
    if (ss['neu'] > ss['pos'] and ss['neu'] > ss['neg']):
        pass
    elif (ss['neg'] > ss['pos']):
        emo="Negative"
        negva = 5 - (5 * ss['neg'])
        if negva > 2.5:
            negva = negva - 2.5
        rating = negva
    else:
        emo="Positive"
        negva = 5 * ss['pos']
        if negva < 2.5:
            negva = negva + 2.5
        rating = negva
    return emo,rating

# python manage.py runserver 192.168.29.145:5000
print(sent("average"))