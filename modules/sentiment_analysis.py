import requests
from textblob import TextBlob
from requests.exceptions import RequestException

class SentimentAnalysis:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_tweets(self, query, count=100):
        url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&max_results={count}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"An error occurred: {e}")
            return {}

    def analyze_sentiment(self, text):
        analysis = TextBlob(text)
        return analysis.sentiment.polarity

    def score_market_sentiment(self, query, count=100):
        tweets = self.fetch_tweets(query, count)
        total_sentiment = 0
        tweet_count = 0

        for tweet in tweets.get('data', []):
            sentiment = self.analyze_sentiment(tweet['text'])
            total_sentiment += sentiment
            tweet_count += 1

        if tweet_count == 0:
            return 0

        average_sentiment = total_sentiment / tweet_count
        return average_sentiment

# Example usage:
# sentiment_analyzer = SentimentAnalysis(api_key='YOUR_TWITTER_API_KEY')
# sentiment_score = sentiment_analyzer.score_market_sentiment('cryptocurrency')
# print(f'Market Sentiment Score: {sentiment_score}')