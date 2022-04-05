from email import header
import requests
import json


url = 'https://mis.taifex.com.tw/futures/api/getQuoteList'

payload = {
    "MarketType": "0",
    "SymbolType": "F",
    "KindID": "1",
    "CID": "TXF",
    "ExpireMonth": "",
    "RowSize": "全部",
    "PageNo": "",
    "SortColumn": "",
    "AscDesc": "A"
}

headers = {
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
}

response = requests.post(url, data=json.dumps(payload), headers=headers)
print(response.json()['RtData']['QuoteList'])
