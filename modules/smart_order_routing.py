from typing import List, Dict
import requests
from requests.exceptions import HTTPError

class SmartOrderRouting:
    def __init__(self, exchanges: List[str], api_keys: Dict[str, str]):
        self.exchanges = exchanges
        self.api_keys = api_keys

    def get_order_book(self, exchange: str) -> Dict:
        try:
            response = requests.get(f'https://api.{exchange}.com/v1/orderbook', headers={'Authorization': self.api_keys[exchange]})
            response.raise_for_status()
            return response.json()
        except HTTPError as err:
            print(f"Failed to fetch order book from {exchange}: {err}")
            return {}

    def find_best_price(self, symbol: str) -> Dict:
        best_price = None
        best_exchange = None

        for exchange in self.exchanges:
            order_book = self.get_order_book(exchange)
            if order_book:
                current_best_price = self.extract_best_price(order_book, symbol)
                if best_price is None or current_best_price < best_price:
                    best_price = current_best_price
                    best_exchange = exchange

        return {
            'best_price': best_price,
            'best_exchange': best_exchange
        }

    def extract_best_price(self, order_book: Dict, symbol: str) -> float:
        # Assuming order_book contains 'bids' and 'asks' for the symbol
        best_bid = max(order_book['bids'], key=lambda x: x['price'])['price']
        best_ask = min(order_book['asks'], key=lambda x: x['price'])['price']
        return best_ask  # Return the best ask price for buying

    def execute_trade(self, exchange: str, symbol: str, amount: float):
        # Placeholder for actual trade execution
        trade_data = {
            'symbol': symbol,
            'amount': amount
        }
        response = requests.post(f'https://api.{exchange}.com/v1/trade', json=trade_data, headers={'Authorization': self.api_keys[exchange]})
        return response.json()

    def route_order(self, symbol: str, amount: float):
        best_price_info = self.find_best_price(symbol)
        if best_price_info['best_price'] is not None:
            self.execute_trade(best_price_info['best_exchange'], symbol, amount)
            return f"Trade executed on {best_price_info['best_exchange']} at price {best_price_info['best_price']}"
        else:
            return "No suitable price found for trade."