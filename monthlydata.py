from flask import Flask, Blueprint, request, jsonify
import requests
from datetime import datetime, timedelta


monthly_blueprint = Blueprint('monthly', __name__)


API_ACCESS_KEY = "14d7e924c0a26766fff2d1d05f2e50a4"
API_BASE_URL = "http://api.marketstack.com/v1/eod"

app = Flask(__name__)

def get_stock_data(stock_name, start_date, end_date):
    stock_params = {
        'access_key': API_ACCESS_KEY,
        'symbols': stock_name,
        'date_from': start_date,
        'date_to': end_date
    }

    try:
        stock_response = requests.get(API_BASE_URL, params=stock_params)
        stock_data = stock_response.json()
        return stock_data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def generate_monthly_dates(start_date, end_date='2023-10-25'):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    monthly_dates = []

    while start_date <= end_date:
        next_month = start_date.replace(day=1) + timedelta(days=31)
        last_day_of_month = (next_month - timedelta(days=1)).replace(day=1)
        monthly_dates.append((start_date, last_day_of_month))
        start_date = next_month

    return monthly_dates

def get_month_key(date):
    return date.strftime('%Y%m')

def get_month_name(date):
    return date.strftime('%B %Y')

@monthly_blueprint.route('/monthly_stock_data', methods=['GET'])
def monthly_stock_data():
    stock_name = request.args.get('stock_symbol', '').upper()
    start_date = request.args.get('start_date', '2023-01-01')
    end_date = request.args.get('end_date', '2023-10-31')  

    if stock_name:
        monthly_date_ranges = generate_monthly_dates(start_date, end_date)

        monthly_stock_data = {}

        for start, end in monthly_date_ranges:
            stock_data = get_stock_data(stock_name, start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
            print("Stock Data:", stock_data)  # Add this line for debugging

            if stock_data and 'error' not in stock_data:
                # Check if the 'data' key exists in the response
                if 'data' in stock_data:
                    # Sort the stock data within each monthly range by date
                    stock_data['data'].sort(key=lambda x: x['date'])
                    month_key = get_month_key(start)
                    month_name = get_month_name(start)
                    monthly_stock_data[month_key] = {
                        'month_name': month_name,
                        'data': stock_data
                    }
                else:
                    return jsonify({'error': 'No data available for the specified date range.'}), 400
            else:
                return jsonify({'error': 'Error fetching stock data.'}), 500

        # Sort the monthly data by month and year
        sorted_monthly_data = dict(sorted(monthly_stock_data.items(), key=lambda item: item[0]))

        return jsonify(sorted_monthly_data), 200
    else:
        return jsonify({'error': 'Stock symbol not provided.'}), 400

if __name__ == '__main__':
    app.run()