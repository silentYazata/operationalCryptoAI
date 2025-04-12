import logging
import os

# Configure the logger
log_file_path = os.path.join(os.path.dirname(__file__), 'trading_bot.log')
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_trade_action(action, details):
    """Logs trade actions with details."""
    logging.info(f"Trade Action: {action}, Details: {details}")

def log_event(event):
    """Logs important events."""
    logging.info(f"Event: {event}")

def log_error(error_message):
    """Logs error messages."""
    logging.error(f"Error: {error_message}")