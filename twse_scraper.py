import requests
import json


response = requests.get(
    'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=20220401&selectType=30&_=1649130620031')
print(response.json()['data'])
