import requests

class DeFiYieldFarming:
    def __init__(self, api_key, staking_platforms):
        self.api_key = api_key
        self.staking_platforms = staking_platforms

    def get_staking_rewards(self, token):
        rewards = {}
        for platform in self.staking_platforms:
            response = requests.get(f"{platform['url']}/rewards?token={token}&api_key={self.api_key}")
            if response.status_code == 200:
                rewards[platform['name']] = response.json().get('rewards', 0)
            else:
                rewards[platform['name']] = None
        return rewards

    def stake_tokens(self, token, amount, platform):
        response = requests.post(f"{platform['url']}/stake", json={
            'token': token,
            'amount': amount,
            'api_key': self.api_key
        })
        return response.json()

    def withdraw_tokens(self, token, amount, platform):
        response = requests.post(f"{platform['url']}/withdraw", json={
            'token': token,
            'amount': amount,
            'api_key': self.api_key
        })
        return response.json()

    def get_yield_farming_status(self, token, platform):
        response = requests.get(f"{platform['url']}/status?token={token}&api_key={self.api_key}")
        if response.status_code == 200:
            return response.json()
        return None

# Example usage
if __name__ == "__main__":
    api_key = "your_api_key"
    staking_platforms = [
        {"name": "Platform A", "url": "https://api.platforma.com"},
        {"name": "Platform B", "url": "https://api.platformb.com"}
    ]
    
    defi_bot = DeFiYieldFarming(api_key, staking_platforms)
    rewards = defi_bot.get_staking_rewards("ETH")
    print(rewards)