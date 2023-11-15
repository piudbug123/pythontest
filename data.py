import requests

url = "http://api.marketstack.com/v1/eod?access_key=14d7e924c0a26766fff2d1d05f2e50a4&symbols=AAPL"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
