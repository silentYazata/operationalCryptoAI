import requests
import json
import logging
from requests.exceptions import HTTPError

class TelegramAlerts:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        logging.basicConfig(level=logging.INFO)

    def send_alert(self, message):
        payload = {
            'chat_id': self.chat_id,
            'text': message,
            'parse_mode': 'Markdown'
        }
        try:
            response = requests.post(self.base_url, data=payload)
            response.raise_for_status()
            logging.info("Alert sent successfully.")
        except HTTPError as err:
            logging.error(f"Failed to send alert: {err}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

    def trade_alert(self, trade_details):
        message = f"Trade Alert:\n*Token:* {trade_details['token']}\n*Action:* {trade_details['action']}\n*Amount:* {trade_details['amount']}\n*Price:* {trade_details['price']}"
        self.send_alert(message)

    def market_update(self, update_details):
        message = f"Market Update:\n*Token:* {update_details['token']}\n*Price:* {update_details['price']}\n*Change:* {update_details['change']}"
        self.send_alert(message)

# Example usage:
# telegram_alerts = TelegramAlerts('YOUR_BOT_TOKEN', 'YOUR_CHAT_ID')
# telegram_alerts.trade_alert({'token': 'BTC', 'action': 'BUY', 'amount': 0.1, 'price': 50000})
# telegram_alerts.market_update({'token': 'ETH', 'price': 4000, 'change': '+5%'})