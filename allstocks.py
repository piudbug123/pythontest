import requests

def get_all_stock_data():
    API_ACCESS_KEY = "14d7e924c0a26766fff2d1d05f2e50a4"  # Replace with your API access key
    API_BASE_URL = "http://api.marketstack.com/v1/symbols"

    stockParams = {
        'access_key': API_ACCESS_KEY
    }

    response = requests.get(API_BASE_URL, params=stockParams)

    if response.status_code == 200:
        stock_data = response.json()
        return stock_data
    else:
        print(f"Failed to retrieve stock data. Status Code: {response.status_code}")
        return None

if __name__ == "__main__":
    stock_data = get_all_stock_data()

    if stock_data:
        print("List of stock symbols and their data:")
        for stock_symbol in stock_data['data']:
            print(stock_symbol)
    else:
        print("Failed to retrieve stock data.")
