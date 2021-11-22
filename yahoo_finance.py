from typing import Union
import requests

class Yahoo_Finance_API():
    
    def __init__(self,api_key:str=None) -> None:
        if api_key is None:
            raise Exception("Input a api key")
        self.api_key = api_key
        self.header = {"X-API-KEY": self.api_key, "Accept": "application/json"}
        
    def get_quote(self,region:str=None,language:str="eng",symbols:str=None) -> dict:
        
        if len(symbols) >10:
            raise Exception("You must have 10 or lesser char in symbol parameter")
        
        if region is None:
            raise Exception("pass a region")
        
        if symbols is None:
            raise Exception("pass a symbol")
        
        symbols = symbols.replace(",","%2C")
        
        response = requests.get(url = f"https://yfapi.net/v6/finance/quote?region={region}&lang={language}&symbols={symbols}",headers=self.header)
        return response.json()

    def get_option_chain(self,date:int=None,symbol:str=None) -> dict:
        
        if symbol is None:
            raise Exception("pass a symbol")
        
        if date is None:
            response = requests.get(url = f"https://yfapi.net/v7/finance/options/{symbol}",headers=self.header)
            return response.json()
        
        elif isinstance(date,int):
            
            response = requests.get(url = f"https://yfapi.net/v7/finance/options/{symbol}?date={date}",headers=self.header)
            return response.json()
    
    def get_stock_history(self,interval:str="1d",range:str="1mo",symbols:str=None) -> dict:
        """[get stock history of stock(s)]

        Args:
            interval (str, optional): [eg. 1m,5m,1d,1wk,1mo]. Defaults to "1d".
            range (str, optional): [eg. 1d,1m,1y,max]. Defaults to "1mo".
            symbols (str, optional): [eg. AAPL]. Defaults to None.

        Returns:
            dict: [response]
        """
        
        if symbols is None:
            raise Exception("pass a symbol")
        
        symbols = symbols.replace(",","%2C")

        response = requests.get(url = f"https://yfapi.net/v8/finance/spark?interval={interval}&range={range}&symbols={symbols}",headers=self.header)
        return response.json()
        

#delete
x= Yahoo_Finance_API("rrjPh7odr7793iWqonsql6NtgXIYjB9T71LtY887")
print(x.get_option_chain(date=8,symbol="aapl"))