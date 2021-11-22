from typing import Union
import requests

class Clash_Of_Clans_API():
    
    def __init__(self,api_key:str) -> None:
        if api_key is None:
            raise Exception("Input a api key")
        self.api_key = api_key
        self.header = {"authorization": f"Bearer {self.api_key}", "Accept": "application/json"}