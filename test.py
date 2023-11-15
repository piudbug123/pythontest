from flask import Blueprint, jsonify
import random

test_blueprint = Blueprint('test', __name__)

def fetch_live_data():
    return {
        "symbol": "AAPL",
        "high": random.uniform(140, 150),
        "low": random.uniform(130, 140)
    }

def per_minute_strategy(high, low):
    if low < 135:
        return 'Buy'
    elif high > 145:
        return 'Sell'
    else:
        return 'Hold'

@test_blueprint.route('/trading', methods=['GET'])
def trading_strategy():
    live_data = fetch_live_data()
    high_price = live_data["high"]
    low_price = live_data["low"]

    signal = per_minute_strategy(high_price, low_price)

    response = {'signal': signal}
    return jsonify(response)
