import requests
from bs4 import BeautifulSoup

class PumpfunGmgnTracker:
    def __init__(self):
        self.pumpfun_url = "https://pumpfun.com/trending"
        self.gmgn_url = "https://gmgn.com/trending"

    def scrape_trending_tokens(self):
        trending_tokens = []
        trending_tokens.extend(self.scrape_pumpfun())
        trending_tokens.extend(self.scrape_gmgn())
        return trending_tokens

    def scrape_pumpfun(self):
        response = requests.get(self.pumpfun_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        tokens = []

        for token in soup.find_all('div', class_='token'):
            token_name = token.find('h3').text
            token_symbol = token.find('span', class_='symbol').text
            tokens.append({'name': token_name, 'symbol': token_symbol})

        return tokens

    def scrape_gmgn(self):
        response = requests.get(self.gmgn_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        tokens = []

        for token in soup.find_all('div', class_='token'):
            token_name = token.find('h3').text
            token_symbol = token.find('span', class_='symbol').text
            tokens.append({'name': token_name, 'symbol': token_symbol})

        return tokens

if __name__ == "__main__":
    tracker = PumpfunGmgnTracker()
    trending_tokens = tracker.scrape_trending_tokens()
    print(trending_tokens)