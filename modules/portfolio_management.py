from typing import List, Dict

class PortfolioManager:
    def __init__(self):
        self.portfolio = {}

    def add_asset(self, asset: str, amount: float, price: float):
        if asset in self.portfolio:
            self.portfolio[asset]['amount'] += amount
            self.portfolio[asset]['total_investment'] += amount * price
        else:
            self.portfolio[asset] = {
                'amount': amount,
                'total_investment': amount * price,
                'average_price': price
            }

    def remove_asset(self, asset: str, amount: float):
        if asset in self.portfolio and self.portfolio[asset]['amount'] >= amount:
            self.portfolio[asset]['amount'] -= amount
            if self.portfolio[asset]['amount'] == 0:
                del self.portfolio[asset]

    def get_portfolio_value(self, current_prices: Dict[str, float]) -> float:
        total_value = 0.0
        for asset, details in self.portfolio.items():
            total_value += details['amount'] * current_prices.get(asset, 0)
        return total_value

    def get_portfolio_summary(self) -> List[Dict[str, float]]:
        summary = []
        for asset, details in self.portfolio.items():
            summary.append({
                'asset': asset,
                'amount': details['amount'],
                'average_price': details['average_price'],
                'total_investment': details['total_investment']
            })
        return summary

    def rebalance_portfolio(self, target_allocations: Dict[str, float], current_prices: Dict[str, float]):
        total_value = self.get_portfolio_value(current_prices)
        for asset, target_percentage in target_allocations.items():
            target_value = total_value * target_percentage
            current_value = self.portfolio.get(asset, {}).get('amount', 0) * current_prices.get(asset, 0)
            if current_value < target_value:
                # Logic to buy more of the asset
                pass
            elif current_value > target_value:
                # Logic to sell some of the asset
                pass

# Example usage:
# portfolio_manager = PortfolioManager()
# portfolio_manager.add_asset('BTC', 0.5, 30000)
# portfolio_manager.add_asset('ETH', 2, 2000)
# print(portfolio_manager.get_portfolio_summary())