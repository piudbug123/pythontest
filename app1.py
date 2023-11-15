from flask import Blueprint, jsonify
from flask import Flask, jsonify
import requests
from app import app

app = Flask(__name__)


top_30_stocks = Blueprint('top_30_stocks', __name__)
monthly_stock_data = Blueprint('monthly_stock_data', __name__)

# Route 1 for top_30_stocks
@top_30_stocks.route('/top_30_stocks', methods=['GET'])
def top_30_stocks_route():
    return jsonify({'message': 'This is the top 30 stocks route'}), 200

# Route 2 for monthly_stock_data
@monthly_stock_data.route('/monthly_stock_data', methods=['GET'])
def monthly_stock_data():
    return jsonify({'message': 'This is the monthly stock data route'}), 200



# # Route 3: Add Numbers
# # @api.route('/add/<int:num1>/<int:num2>', methods=['GET'])
# # def add_numbers(num1, num2):
# #     result = num1 + num2
# #     return jsonify({'result': result}), 200

if __name__ == '__main__':
    app.run(debug=True)