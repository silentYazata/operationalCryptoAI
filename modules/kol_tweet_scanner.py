import tweepy
import re

class KOLTweetScanner:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        self.auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def extract_contract_addresses(self, tweet):
        # Regular expression to find Ethereum contract addresses
        pattern = r'0x[a-fA-F0-9]{40}'
        return re.findall(pattern, tweet)

    def scan_tweets(self, usernames, count=10):
        contract_addresses = []
        for username in usernames:
            try:
                tweets = self.api.user_timeline(screen_name=username, count=count, tweet_mode='extended')
                for tweet in tweets:
                    addresses = self.extract_contract_addresses(tweet.full_text)
                    contract_addresses.extend(addresses)
            except tweepy.TweepError as e:
                print(f"Error fetching tweets for {username}: {e}")
        return contract_addresses

# Example usage:
# scanner = KOLTweetScanner(api_key='YOUR_API_KEY', api_secret_key='YOUR_API_SECRET', access_token='YOUR_ACCESS_TOKEN', access_token_secret='YOUR_ACCESS_TOKEN_SECRET')
# addresses = scanner.scan_tweets(['KOL_username1', 'KOL_username2'])
# print(addresses)