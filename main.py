import requests
import time

# API_KEY = 'your_api_key'
# API_SECRET = 'your_api_secret'
access_key = '14d7e924c0a26766fff2d1d05f2e50a4'
symbols = 'AAPL'
BASE_URL = 'http://api.marketstack.com/v1/eod?access_key=fd6f0bc2cae94c52d515535349fdcde9&symbols=AAPL'  # Replace with your trading platform's API URL


SMA_SHORT_PERIOD = 10
SMA_LONG_PERIOD = 50


def get_price(symbol):
    
    response = requests.get(f'{BASE_URL}/ticker/{symbol}')
    data = response.json()
    return data['price']

def calculate_sma(symbol, period):
    
    return 0.0

def main():
    while True:
        try:
            symbol = 'AAPL'  
            short_sma = calculate_sma(symbol, SMA_SHORT_PERIOD)
            long_sma = calculate_sma(symbol, SMA_LONG_PERIOD)
            current_price = get_price(symbol)

            if short_sma > long_sma and current_price > short_sma:
                
                print(f'Buy {symbol} at {current_price}')
            elif short_sma < long_sma and current_price < short_sma:
                
                print(f'Sell {symbol} at {current_price}')
            else:
                print(f'Hold {symbol} at {current_price}')

            time.sleep(60)  # Check the strategy every minute
        except Exception as e:
            print(f'An error occurred: {e}')
            time.sleep(60)  # Wait for a minute before retrying

if __name__ == "__main__":
    main()

