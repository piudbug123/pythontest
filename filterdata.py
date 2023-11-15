import requests
# import schedule
# import time

# def fetch_and_apply_strategy():
api_url = "http://api.marketstack.com/v1/eod"
api_params = {
    'access_key': '14d7e924c0a26766fff2d1d05f2e50a4',
    'symbols': 'AAPL'
}

response = requests.get(api_url, params=api_params)

if response.status_code == 200:
    api_response = response.json()                                                                    
    for stock_data in api_response['data']:
        print('Ticker %s has a day high of %s and a volume of %s on %s' % (
            stock_data['symbol'],
            stock_data['high'],
            stock_data['volume'],
            stock_data['date']
        ))
    
   
    pagination_data = api_response['pagination']
    print('Pagination data:')
    print('Limit:', pagination_data['limit'])
    print('Count:', pagination_data['count'])
    print('Total:', pagination_data['total'])
else:
    print('Failed to fetch data from the API. Status code:', response.status_code)

#     schedule.every(1).minutes.do(fetch_and_apply_strategy)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
