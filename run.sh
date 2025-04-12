#!/bin/bash

# Navigate to the project directory
cd "$(dirname "$0")"

# Activate the virtual environment
source venv/bin/activate

# Run database migrations
bash database/migrate.sh

# Start the trading bot
python3 modules/trading_bot.py &

# Start the Telegram alerts service
python3 modules/telegram_alerts.py &

# Start the web dashboard
python3 modules/crypto_dashboard.py &

# Start the sentiment analysis service
python3 modules/sentiment_analysis.py &

# Start the market maker bot
python3 modules/market_maker.py &

# Start the DEX trading integration
python3 modules/dex_trading.py &

# Start the arbitrage trading bot
python3 modules/arbitrage_trading.py &

# Start the portfolio management service
python3 modules/portfolio_management.py &

# Wait for all background processes to finish
wait

# Deactivate the virtual environment
deactivate