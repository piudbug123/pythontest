import requests
from flask import Flask, Blueprint, request, jsonify, render_template

indicator_blueprint = Blueprint('indicator', __name__)

app = Flask(__name__)

# Replace with your actual API endpoint for stock data
STOCK_API_URL = "http://api.marketstack.com/v1/eod"  # Check this URL

@indicator_blueprint.route('/indicator', methods=['GET', 'POST'])
def indicator():
    if request.method == 'POST':
        symbol = request.form.get('symbol')

        if not symbol:
            return jsonify({'error': 'Symbol data is missing.'}), 400

        price_data = get_stock_data(symbol)

        if not price_data:
            return jsonify({'error': 'Failed to fetch stock data.'}), 400

        high = price_data['high']
        low = price_data['low']
        signal = generate_signal(high, low)

        response = {'signal': signal}
        return jsonify(response)
    
    # Render an HTML form for user input
    # return render_template('indicator_form.html')

def get_stock_data(symbol):
  
    try:
        params = {'access_key': '14d7e924c0a26766fff2d1d05f2e50a4', 'symbols': symbol}
        response = requests.get(STOCK_API_URL, params=params)  # Check the URL and params
        data = response.json()
        if 'data' in data:
            return data['data'][0]
    except Exception as e:
        print(e)
    return None

def generate_signal(high, low):
    # Modify this indicator logic based on high and low prices
    if high > low:
        return 'Buy'
    else:
        return 'Sell'

