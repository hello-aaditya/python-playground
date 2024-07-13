import requests

def fetch_random_stocks_data():
    url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"
    response = requests.get(url)
    data = response.json()

    if data['success'] and 'data' in data:
        stock_data = data['data']
        stock_name = stock_data['Name']
        stock_symbol = stock_data['Symbol']
        cap = stock_data['MarketCap']
        price = stock_data['CurrentPrice']
        return stock_name, stock_symbol, cap, price
    
    else:
        raise Exception('failed to fetch stock data')
    
def main():
    try:
        stock_name, stock_symbol, cap, price = fetch_random_stocks_data()
        print(f'Name: {stock_name}\nSymbol: {stock_symbol}\nMarket Cap: {cap}\nCurrent Price: {price}')
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()