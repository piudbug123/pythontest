from flask import Blueprint, request, jsonify
import requests

stocks_blueprint = Blueprint('stocks', __name__)

API_ACCESS_KEY = "14d7e924c0a26766fff2d1d05f2e50a4"
API_BASE_URL = "http://api.marketstack.com/v1/eod"

@stocks_blueprint.route('/stock_data', methods=['GET'])
def stock_data():
    stock_symbol = request.args.get('stock_symbol', '').upper()

    if stock_symbol:
        stock_data = get_stock_data(stock_symbol)

        if stock_data and 'error' not in stock_data:
            return jsonify(stock_data), 200
        else:
            return jsonify({'error': 'Failed to retrieve stock data.'}), 400
    else:
        return jsonify({'error': 'Stock symbol not provided.'}), 400

def get_stock_data(stock_symbol):
    stock_params = {
        'access_key': API_ACCESS_KEY,
        'symbols': stock_symbol
    }

    try:
        response = requests.get(API_BASE_URL, params=stock_params)
        stock_data = response.json()
        return stock_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
