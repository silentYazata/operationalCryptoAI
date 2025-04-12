from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/performance')
def performance():
    # Placeholder for performance data
    data = {
        'total_trades': 100,
        'successful_trades': 80,
        'failed_trades': 20,
        'profit_loss': 1500.00
    }
    return jsonify(data)

@app.route('/api/market_data')
def market_data():
    # Placeholder for market data
    market_data = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd').json()
    return jsonify(market_data)

if __name__ == '__main__':
    app.run(debug=True)