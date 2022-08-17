# This python file is to pull names of top 200 cryptocurrencies from coinmarketcap
# Author: Mingxi Chen Mx.Chen.official@outlook.com

import csv
from requests import Request, Session
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
parameter = {'limit': '200', 'sort': 'cmc_rank'}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'YOUR COINMARKET CAP API KEY'

}
session = Session()
session.headers.update(headers)
response = session.get(url, params=parameter)
info = json.loads(response.text)

top200 = []
for index in range(200):
    top200.append(info['data'][index]['symbol'])

with open('csvfile.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(top200)
