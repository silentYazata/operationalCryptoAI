import requests

class CopyTradingBot:
    def __init__(self, api_key, user_id):
        self.api_key = api_key
        self.user_id = user_id
        self.followed_traders = []
        self.trades = []

    def follow_trader(self, trader_id):
        if trader_id not in self.followed_traders:
            self.followed_traders.append(trader_id)
            print(f"Now following trader: {trader_id}")

    def unfollow_trader(self, trader_id):
        if trader_id in self.followed_traders:
            self.followed_traders.remove(trader_id)
            print(f"Unfollowed trader: {trader_id}")

    def fetch_trader_trades(self, trader_id):
        # Simulated API call to fetch trades of a followed trader
        response = requests.get(f"https://api.tradingplatform.com/traders/{trader_id}/trades", headers={"Authorization": f"Bearer {self.api_key}"})
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch trades for trader {trader_id}: {response.status_code}")
            return []

    def execute_trade(self, trade):
        # Simulated trade execution logic
        print(f"Executing trade: {trade}")

    def copy_trades(self):
        for trader_id in self.followed_traders:
            trader_trades = self.fetch_trader_trades(trader_id)
            for trade in trader_trades:
                self.execute_trade(trade)
                self.trades.append(trade)

    def get_copied_trades(self):
        return self.trades

# Example usage
if __name__ == "__main__":
    bot = CopyTradingBot(api_key="your_api_key", user_id="your_user_id")
    bot.follow_trader("trader123")
    bot.copy_trades()
    print(bot.get_copied_trades())