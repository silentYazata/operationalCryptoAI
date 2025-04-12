from flask import Flask, request, jsonify
from flask_cors import CORS
from modules.trading_bot import TradingBot
from database.database_config import DatabaseConfig

app = Flask(__name__)
CORS(app)

trading_bot = TradingBot()

@app.route('/api/trade', methods=['POST'])
def execute_trade():
    data = request.json
    token = data.get('token')
    amount = data.get('amount')
    
    if not token or not amount:
        return jsonify({'error': 'Token and amount are required'}), 400
    
    try:
        result = trading_bot.execute_trade(token, amount)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/status', methods=['GET'])
def get_status():
    status = trading_bot.get_status()
    return jsonify(status), 200

@app.route('/api/history', methods=['GET'])
def get_trade_history():
    connection = DatabaseConfig().connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM trades ORDER BY trade_time DESC")
    trades = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return jsonify(trades), 200

if __name__ == '__main__':
    app.run(debug=True)