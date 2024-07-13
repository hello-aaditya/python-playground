
```markdown
# Python API Projects

This repository contains three Python projects that demonstrate how to handle API requests. Each project fetches different types of data from an API and processes it. The projects are:

1. Fetching Random User Data
2. Fetching Random Stock Data
3. Fetching Random User Data with Detailed Attributes

## Requirements

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```bash
pip install requests
```

## Project 1: Fetch Random User Data

This project fetches a random user's username and country from the Free API.

### Code

```python
import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data['success'] and 'data' in data:
        user_data = data['data']
        username = user_data['login']['username']
        country = user_data['location']['country']
        return username, country
    else:
        raise Exception('Failed to fetch user data')

def main():
    try:
        username, country = fetch_random_user_freeapi()
        print(f"Username: {username}\nCountry: {country}")
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()
```

## Project 2: Fetch Random Stock Data

This project fetches random stock data, including stock name, symbol, market cap, and current price.

### Code

```python
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
        raise Exception('Failed to fetch stock data')

def main():
    try:
        stock_name, stock_symbol, cap, price = fetch_random_stocks_data()
        print(f'Name: {stock_name}\nSymbol: {stock_symbol}\nMarket Cap: {cap}\nCurrent Price: {price}')
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()
```

## Project 3: Fetch Random User Data with Detailed Attributes

This project is similar to Project 1 but includes handling more detailed user attributes.

### Code

```python
import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data['success'] and 'data' in data:
        user_data = data['data']
        username = user_data['login']['username']
        country = user_data['location']['country']
        return username, country
    else:
        raise Exception('Failed to fetch user data')

def main():
    try:
        username, country = fetch_random_user_freeapi()
        print(f"Username: {username}\nCountry: {country}")
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()
```

## How to Run the Projects

1. Clone this repository.
2. Navigate to the project directory.
3. Ensure you have Python 3.x installed.
4. Install the `requests` library if not already installed: `pip install requests`
5. Run the desired project script:
   ```bash
   python project_script_name.py
   ```
   Replace `project_script_name.py` with the actual script file name you want to run.


