from abc import ABC, abstractmethod
import time
from datetime import datetime, timezone

class StockPrice:
    def __init__(self, symbol: str, price: float, timestamp: str = None):
        self.symbol = symbol
        self.price = price
        self.timestamp =  timestamp if timestamp is not None else datetime.fromtimestamp(time.time()).astimezone().isoformat()

    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class StockAPI(ABC):
    @abstractmethod
    def get_stock_price(self, symbol: str) -> StockPrice:
        """Fetch the current stock price for the given symbol."""
        pass

    def get_stock_price_list(self, symbol_list: list[str]) -> list[StockPrice]:
        """Fetch the current stock price for the given list of symbols."""
        pass

    @abstractmethod
    def get_historical_data(self, symbol: str, start_date: str, end_date: str) -> list:
        """Fetch historical stock data for the given symbol between start_date and end_date."""
        pass

    
