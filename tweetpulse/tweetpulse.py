import nltk
from translator.translator import Translator

nltk.download('vader_lexicon')
import tweepy
from nltk.sentiment import SentimentIntensityAnalyzer
import csv

# Fill in your Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Search for tweets with the hashtag "Rijkswaterstaat"
search_query = "#Rijkswaterstaat"
#tweets = tweepy.Cursor(api.search_tweets, q=search_query, lang="en").items(10)

# List of tweets
tweets = ["Rijkswaterstaat gaat in juni starten met het vervangen van een viaduct in #Rotterdam. Het viaduct gaat vervangen worden door een tunnel.",
          "Grote kans dat er vanavond sprake is van files rondom #Rijkswaterstaat in #Utrecht vanwege werkzaamheden op de snelweg.",
          "Rijkswaterstaat waarschuwt voor hoogwater in #Zeeland door aanhoudende regenval.",
          "Rijkswaterstaat heeft een nieuwe oeverbescherming aangelegd in #Delfzijl om overstromingen tegen te gaan.",
          "Rijkswaterstaat gaat de komende maanden aan de slag met het verbeteren van de vaarwegen in #Friesland.",
          "Rijkswaterstaat start volgende week met werkzaamheden aan een dijk in #Groningen.",
          "Rijkswaterstaat waarschuwt voor gevaarlijke situaties op het water in #Noord-Holland door harde wind.",
          "Rijkswaterstaat start volgende maand met de aanleg van een nieuwe brug over de rivier de #Maas.",
]



# Initialize Translator

# List of tweets in Dutch
tweets_nl = ["Ik haat Rijkswaterstaat.",
             "Grote kans dat er vanavond sprake is van files rondom #Rijkswaterstaat in #Utrecht vanwege werkzaamheden op de snelweg.",
             "Rijkswaterstaat waarschuwt voor hoogwater in #Zeeland door aanhoudende regenval."]


from googletrans import Translator

# Translate the tweets to English
tweets_en = [Translator().translate(tweet) for tweet in tweets_nl]# Print the translated tweets
for tweet in tweets_en:
    print(tweet)



# Open a new CSV file and write the tweets and their sentiments to it
with open('Rijkswaterstaat_tweets.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Username', 'Tweet Text', 'Timestamp','Sentiment'])
    for tweet in tweets_en:
        sentiment = sia.polarity_scores(tweet.text)
        writer.writerow(["tweet.user.screen_name", tweet, "tweet.created_at", sentiment])

print("Tweets exported to CSV file successfully!")