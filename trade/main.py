from .api.twelvedataapi import TwelveDataAPI
from .api.stockapi import StockPrice
import json

def main():
    print("Trade module main function")
    api = TwelveDataAPI("90bec2a2d41643c598a679b3dd9def5e")
    stock_data = api.get_stock_price_list(["AAPL","NVDA"])
    print(json.dumps([stock.to_json() for stock in stock_data]))

if __name__ == "__main__":
    main()