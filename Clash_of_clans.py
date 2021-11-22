from typing import Union
import requests

class Clash_Of_Clans_API():
    
    def __init__(self,api_key:str=None) -> None:
        if api_key is None:
            raise Exception("Input a api key")
        self.api_key = api_key
        self.header = {"authorization": f"Bearer {self.api_key}", "Accept": "application/json"}
    
    def handle_response(self,response) -> Union[dict,str]:
        bad_response_codes = {0:"No resonse from server",400:"Client provided incorrect parameters for the request.",403:"Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.",404:"Resource was not found.",429:"Request was throttled, because amount of requests was above the threshold defined for the used API token.",500:"Unknown error happened when handling the request.",503:"Service is temprorarily unavailable because of maintenance."}
        if response.status_code == 200:
            return response.json()
        elif response.status_code != 200:
            try:
                response_dict = response.json()
                reason = response_dict["reason"]
                message = response_dict["message"]
                raise Exception(f"{bad_response_codes[response.status_code]} Error status code [{response.status_code}]. Reason: {reason}. Message: {message}")
            except:
                raise Exception(f"{bad_response_codes[response.status_code]} Error status code [{response.status_code}].")
                