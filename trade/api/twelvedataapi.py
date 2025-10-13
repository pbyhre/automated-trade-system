from .stockapi import StockAPI, StockPrice
import requests
import time
from datetime import datetime, timezone

class TwelveDataAPI(StockAPI):
    BASE_URL = "https://api.twelvedata.com"

    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            "Accept": "application/json",
            "Authorization": f"apikey {self.api_key}"
        }

    def get_stock_price(self, symbol):
        url = f"{self.BASE_URL}/price"
        params = {
            "symbol": symbol
        }
        response = requests.get(url, headers=self.headers, params=params)
        return StockPrice(symbol, float(response.json().get("price", 0.0)))
    
    def get_stock_price_list(self, symbol_list):
        prices = []
        url = f"{self.BASE_URL}/price"
        params = {
            "symbol": ",".join(symbol_list)  # Assuming the API supports comma-separated symbols
        }
        response = requests.get(url, headers=self.headers, params=params)
        ts = datetime.fromtimestamp(time.time()).astimezone().isoformat()
        for symbol in symbol_list:
            price = float(response.json().get(symbol, {}).get("price", 0.0))
            prices.append(StockPrice(symbol, price, timestamp=ts))

        return prices

    def get_historical_data(self, symbol, start_date, end_date):
        url = f"{self.BASE_URL}/time_series"
        params = {
            "symbol": symbol,
            "start_date": start_date,
            "end_date": end_date,
            "interval": "1day"
        }
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()