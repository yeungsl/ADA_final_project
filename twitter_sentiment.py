from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

twitter_text = pd.read_csv("./data/trump_twitters.csv", low_memory=False)

print(twitter_text.describe())

# sentences = ["lalalal", "super"]

# analyzer = SentimentIntensityAnalyzer()

# for s in sentences:
#     vs = analyzer.polarity_scores(s)
#     print("{:-<65} {}".format(s, str(vs)))
