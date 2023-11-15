import requests
from flask import Flask, Blueprint, request, jsonify

allstocksdata_blueprint = Blueprint('allstocksdata', __name__)
app = Flask(__name__)

API_ACCESS_KEY = "14d7e924c0a26766fff2d1d05f2e50a4"
API_BASE_URL = "http://api.marketstack.com/v1/eod"

app = Flask(__name__)

# List of all the stock symbols you want to fetch data for
all_stock_symbols = ['AAPL', 'GOOGL', 'TSLA', 'MSFT', 'AMZN', 'AAPL', 'GOOG', 'NFLX', 'NVDA', 'PYPL', 'INTC', 'ADBE', 'CMCSA', 'CSCO', 'AVGO', 'TMUS', 'COST', 'PEP', 'QCOM', 'AMGN', 'COST', 'PEP', 'CSCO', 'AVGO', 'TMUS', 'AMGN', 'GILD', 'INTU', 'SBUX', 'VRTX']

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

@allstocksdata_blueprint.route('/all_stocks', methods=['GET'])
def all_stocks():
    stock_data = {}

    for symbol in all_stock_symbols:
        stock_data[symbol] = get_stock_data(symbol)

    return jsonify(stock_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
