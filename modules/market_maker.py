import time
import random

class MarketMaker:
    def __init__(self, trading_api, market_data_api, spread=0.01, inventory_limit=100):
        self.trading_api = trading_api
        self.market_data_api = market_data_api
        self.spread = spread
        self.inventory_limit = inventory_limit
        self.inventory = {}

    def get_market_price(self, token):
        return self.market_data_api.get_current_price(token)

    def place_order(self, token, order_type, amount, price):
        if order_type == 'buy':
            self.trading_api.buy(token, amount, price)
        elif order_type == 'sell':
            self.trading_api.sell(token, amount, price)

    def manage_inventory(self, token, amount):
        if token in self.inventory:
            self.inventory[token] += amount
        else:
            self.inventory[token] = amount

        if self.inventory[token] > self.inventory_limit:
            self.place_order(token, 'sell', self.inventory[token] - self.inventory_limit, self.get_market_price(token) * (1 + self.spread))

    def run(self, tokens):
        while True:
            for token in tokens:
                market_price = self.get_market_price(token)
                buy_price = market_price * (1 - self.spread)
                sell_price = market_price * (1 + self.spread)

                self.place_order(token, 'buy', random.uniform(1, 10), buy_price)
                self.place_order(token, 'sell', random.uniform(1, 10), sell_price)

                self.manage_inventory(token, random.uniform(-5, 5))

            time.sleep(10)  # Wait before the next cycle

# Example usage:
# trading_api = TradingAPI()  # This should be your trading API instance
# market_data_api = MarketDataAPI()  # This should be your market data API instance
# market_maker = MarketMaker(trading_api, market_data_api)
# market_maker.run(['BTC', 'ETH', 'LTC'])  # List of tokens to trade