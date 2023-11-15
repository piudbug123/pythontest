import requests
import datetime
from pytz import timezone

def is_trading_time():
    eastern = timezone('US/Eastern')
    current_time = datetime.datetime.now(eastern).time()
    trading_start_time = datetime.time(9, 30)
    trading_end_time = datetime.time(16, 0)

    return trading_start_time <= current_time <= trading_end_time

def is_market_open(stock_symbol):
    # Define the API endpoint with the stock symbol
    API_ACCESS_KEY = "14d7e924c0a26766fff2d1d05f2e50a4"
    API_BASE_URL = f"http://api.marketstack.com/v1/eod?access_key={API_ACCESS_KEY}&symbols={stock_symbol}"

    try:
        response = requests.get(API_BASE_URL)
        stock_data = response.json()
        
        # Check if the data is available and the market is open
        return 'data' in stock_data and len(stock_data['data']) > 0

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    stock_symbol = input("Enter the stock symbol (e.g., GOOGL): ").upper()

    if is_trading_time() and is_market_open(stock_symbol):
        print("It's a good time for trading.")
    else:
        print("The market is closed now or the provided stock symbol is not trading.")
