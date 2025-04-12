import requests

class TokenVerifier:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.coingecko.com/api/v3"

    def verify_token(self, token_address):
        """Verify the authenticity of a token using its address."""
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(f"{self.base_url}/coins/ethereum/contract/{token_address}", headers=headers)
        if response.status_code == 200:
            token_data = response.json()
            return {
                "name": token_data.get("name"),
                "symbol": token_data.get("symbol"),
                "verified": True
            }
        else:
            return {
                "name": None,
                "symbol": None,
                "verified": False
            }

# Example usage
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    verifier = TokenVerifier(api_key)
    token_info = verifier.verify_token("0xYourTokenAddressHere")
    print(token_info)