"""  
MIT License

Copyright (c) 2021 Ruthle55Owo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
import requests
from typing import Union
from datetime import date as get_run_date

class Weather_API():
    
    def __init__(self,api_key:str=None) -> None:
        if api_key is None:
            raise Exception("Input a api key")
        self.api_key = api_key
    
    def handle_response(self,response) -> Union[str,dict]:
        """[DO NOT USE!!!!]
        """
        bad_response_codes = {1002:"API key not provided.",1003:"Parameter 'country' not provided.",1005:"API request url is invalid",1006:"No location found matching parameter 'country', try using the fullname and no short variations of the country name.",2006:"API key provided is invalid",2007:"API key has exceeded calls per month quota.",2008:"API key has been disabled.",9999:"Internal application error."}
        if response.status_code == 200:
            return response.json()
        elif response.status_code != 200:
            response_dict = response.json()
            response_dict = response_dict["error"]
            code = response_dict["code"]
            try:
                
                message = response_dict["message"]
                raise Exception(f"{bad_response_codes[code]} Error status code [{response.status_code}]. Error code {code}. Message: {message}")
            except:
                raise Exception(f"{bad_response_codes[code]} Error status code [{response.status_code}].")
    
    def get_current_weather(self,country:str=None,aqi:bool=True) -> Union[str,dict]:
        """[get current weather of a country]

        Args:
            country (str, optional): [enter a country's full name]. Defaults to None.
            aqi (bool, optional): [air quality index True will be yes and False will be no]. Defaults to True.

        Returns:
            Union[str,dict]: [returns current weather]
        """
        if country is None:
            raise Exception("Need a country")
        if len(country) <=2:
            raise Exception("Need the full name of the country")
        if aqi is True:
            aqi = "yes"
        elif aqi is False:
            aqi = "no"
        else:
            raise Exception("aqi needs to either be True or False")
        
        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={country}&aqi={aqi}")
        return self.handle_response(response=response)
    
    def get_weather_forecast(self,country:str=None,aqi:bool=True,days:int = 1,alerts:str = "no") -> Union[str,dict]:
        """[Get weather forecast]

        Args:
            country (str, optional): [enter a country's full name]. Defaults to None.
            aqi (bool, optional): [air quality index True will be yes and False will be no]. Defaults to True.
            days (int, optional): [How many days]. Defaults to 1.
            alerts (str, optional): [any alerts?]. Defaults to "no".

        Returns:
            Union[str,dict]: [returns weather forecast]
        """
        if country is None:
            raise Exception("Need a country")
        if len(country) <=2:
            raise Exception("Need the full name of the country")
        
        if aqi is True:
            aqi = "yes"
        elif aqi is False:
            aqi = "no"
        else:
            raise Exception("aqi needs to either be True or False")
    
        response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={self.api_key}&q={country}&days={days}&aqi={aqi}&alerts={alerts}")
        return self.handle_response(response=response)

    def get_specific_locations_in_specified_country(self,country:str=None) -> Union[str,dict]:
        """[Get some locations in a country or region]

        Args:
            country (str, optional): [enter a country's full name]. Defaults to None.
            
        Returns:
            Union[str,dict]: [returns specific locations which you can use to get weather details]
        """
        if country is None:
            raise Exception("Need a country")
        if len(country) <=2:
            raise Exception("Need the full name of the country")

        response = requests.get(f"http://api.weatherapi.com/v1/search.json?key={self.api_key}&q={country}")
        return self.handle_response(response=response)

    def get_historical_data(self,country:str=None,date:str=None) -> Union[str,dict]:
        """[Get historical data of a country]

        Args:
            country (str, optional): [enter a country's full name]. Defaults to None.
            date (str, optional): [Need a date in yyyy-MM-dd format]. Defaults to None.

        Returns:
            Union[str,dict]: [returns historical data]
        """
        if country is None:
            raise Exception("Need a country")
        if len(country) <=2:
            raise Exception("Need the full name of the country")
        if date is None:
            get_date = get_run_date.today()
            get_date.strftime("%Y-%m-%d")
            date = str(get_date)
        if "-" not in date:
            raise Exception("Need a date in yyyy-MM-dd format")
            
        response = requests.get(f"http://api.weatherapi.com/v1/search.json?key={self.api_key}&q={country}")
        return self.handle_response(response=response)
    
    def get_astronomy(self,country:str=None,date:str=None) -> Union[str,dict]:
        """[Get info of a country sunset, sunrise etc.]

        Args:
            country (str, optional): [enter a country's full name]. Defaults to None.
            date (str, optional): [Need a date in yyyy-MM-dd format]. Defaults to None.
            
        Returns:
            Union[str,dict]: [returns sunset, sunrise etc. data of a country]
        """
        if country is None:
            raise Exception("Need a country")
        if len(country) <=2:
            raise Exception("Need the full name of the country")
        if date is None:
            get_date = get_run_date.today()
            get_date.strftime("%Y-%m-%d")
            date = str(get_date)
        if "-" not in date:
            raise Exception("Need a date in yyyy-MM-dd format")
            
        response = requests.get(f"http://api.weatherapi.com/v1/astronomy.json?key={self.api_key}&q=singapore&dt={date}")
        return self.handle_response(response=response)
    
    def get_time_zone(self,country:str=None) -> Union[str,dict]:
        """[Get time zone of a country]

        Args:
            country (str, optional): [enter a country's full name]. Defaults to None.

        Returns:
            Union[str,dict]: [returns timezone]
        """
        if country is None:
            raise Exception("Need a country")
        if len(country) <=2:
            raise Exception("Need the full name of the country")
        
        response = requests.get(f"http://api.weatherapi.com/v1/timezone.json?key={self.api_key}&q={country}")
        return self.handle_response(response=response)