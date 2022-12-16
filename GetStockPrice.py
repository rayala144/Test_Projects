import urllib.request
import json


def getStockPrice(cmpnyCode):
    resp = urllib.request.urlopen(
        f'https://query2.finance.yahoo.com/v10/finance/quoteSummary/{cmpnyCode}?modules=price')
    data = json.loads(resp.read())
    price = data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
    return price


if __name__ == '__main__':
    price = getStockPrice('nflx')
    print(price)
