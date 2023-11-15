import http.server
import json
from datetime import datetime, timedelta
from urllib.parse import urlparse, parse_qs
import requests

API_ACCESS_KEY = "14d7e924c0a26766fff2d1d05f2e50a4"
API_BASE_URL = "http://api.marketstack.com/v1/eod"

class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path

        if path == '/stocks_data':
            query_params = parse_qs(parsed_url.query)
            stock_symbol = query_params.get('stock_symbol', [''])[0].upper()


            if stock_symbol:
                stock_data = self.get_stocks_data(stock_symbol)

                if stock_data and 'error' not in stock_data:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(stock_data, indent=4).encode())
                else:
                    self.send_response(400)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': 'Failed to retrieve stock data.'}, indent=4).encode())
            else:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Stock symbol not provided.'}, indent=4).encode())
        else:
            super().do_GET()

    def get_stocks_data(self, stock_name):
        stock_params = {
            'access_key': API_ACCESS_KEY,
            'symbols': stock_name
        }

        try:
            stock_response = requests.get(API_BASE_URL, params=stock_params)
            stock_data = stock_response.json()
            return stock_data

        except requests.exceptions.RequestException as e:
            return None

if __name__ == '__main__':
    server_address = ('', 5000)
    httpd = http.server.HTTPServer(server_address, CustomRequestHandler)
    print('Server started at http://localhost:5000/')
    httpd.serve_forever()
