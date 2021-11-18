from typing import Union
import requests

class Brawl_Stars():

    def __init__(self,api_key:str) -> None:
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
                raise Exception(f"{bad_response_codes[response.status_code]} Error code [{response.status_code}]. Reason: {reason}. Message: {message}")
            except:
                raise Exception(f"{bad_response_codes[response.status_code]} Error code [{response.status_code}].")
                
    def get_player_stats(self,player_id:str = None) -> Union[dict,str]:
        """[Get a player's stats]

        Args:
            player_id (str): [MUST BE GIVEN]

        Returns:
            dict | str: [returns either an error with the error message and code or a dictionary of the player's stats]
        """
        if player_id == None:
            raise Exception("Give a player id")

        player_id = player_id.replace("#","")
        response = requests.get(f"https://api.brawlstars.com/v1/players/%23{player_id}",headers=self.header)
        return self.handle_response(response=response)

    def get_player_battle_logs(self,player_id:str = None) -> Union[dict,str]:
        """[Get the battle logs of a player, this may take up to 30min to update]

        Args:
            player_id (str): [MUST BE GIVEN]

        Returns:
            dict | str: [returns either an error with the error message and code or a dictionary of the player's battle logs]
        """
        if player_id == None:
            raise Exception("Give a player id")
            
        player_id = player_id.replace("#","")
        response = requests.get(f"https://api.brawlstars.com/v1/players/%23{player_id}/battlelog",headers=self.header)
        return self.handle_response(response=response)

    def get_club(self,club_id:str = None) -> Union[dict,str]:
        """[Get the details of a club]

        Args:
            club_id (str): [MUST BE GIVEN]

        Returns:
            dict | str: [returns either an error with the error message and code or a dictionary of the club's stats]
        """
        if club_id == None:
            raise Exception("Give a club id")
        club_id = club_id.replace("#","")
        response = requests.get(f"https://api.brawlstars.com/v1/clubs/%23{club_id}",headers=self.header)
        return self.handle_response(response=response)

    def get_club_members(self,club_id:str = None) -> Union[dict,str]:
        """[Get a list of all the members of a club]

        Args:
            club_id (str): [MUST BE GIVEN]

        Returns:
            dict | str: [returns either an error with the error message and code or a dictionary of the members in a club]
        """
        if club_id == None:
            raise Exception("Give a club id")
        
        club_id = club_id.replace("#","")
        response = requests.get(f"https://api.brawlstars.com/v1/clubs/%23{club_id}/members",headers=self.header)
        return self.handle_response(response=response)
    
    def get_current_events(self) -> Union[str,dict]:
        """[Get the current events]

        Returns:
            str | dict: [returns either an error with the error message and code or a dictionary of current events]
        """
        response = requests.get(f"https://api.brawlstars.com/v1/events/rotation",headers=self.header)
        return self.handle_response(response=response)

    def get_brawlers(self) -> Union[str,dict]:
        """[Get the current brawlers and a description of them]

        Returns:
            str | dict: [returns either an error with the error message and code or a dictionary of the brawlers]
        """
        response = requests.get(f"https://api.brawlstars.com/v1/brawlers",headers=self.header)
        return self.handle_response(response=response)
    
    def get_top_players(self,countryCode = "global") -> Union[str,dict]:
        """[Get top players with country code with either the 2 letters of the country such as SG or for a phone number like +65 would be written as 65 or it could be left as the default 'global'.]

        Args:
            countryCode (str | int): [if left as empty will return the global top ranks]

        Returns:
            dict | str: [returns either an error with the error message and code or a dictionary of the players]
        """
        if isinstance(countryCode,(str,int)) == False:
            raise Exception("Only a str or int type is allowed.")
         
        countryCode = str(countryCode).replace("+","")
        response = requests.get(f"https://api.brawlstars.com/v1/rankings/{countryCode}/players",headers=self.header)
        return self.handle_response(response=response)

    def get_top_clubs(self,countryCode = "global") -> Union[str,dict]:
        """[Get top clubs with country code with either the 2 letters of the country such as SG or for a phone number like +65 would be written as 65 or it could be left as the default 'global'.]

        Args:
            countryCode (str | int): [if left as empty will return the global top ranks]

        Returns:
            dict | str: [returns either an error with the error message and code or a dictionary of the top clubs]
        """
        
        if isinstance(countryCode,(str,int)) == False:
            raise Exception("Only a str or int type is allowed.")
         
        countryCode = str(countryCode).replace("+","")
        response = requests.get(f"https://api.brawlstars.com/v1/rankings/{countryCode}/clubs",headers=self.header)
        return self.handle_response(response=response)

    def get_top_brawlers(self,countryCode = "global",brawler: str = None) -> Union[str,dict]:
        """[Get top brawlers with country code with either the 2 letters of the country such as SG or for a phone number like +65 would be written as 65 or it could be left as the default 'global'.]

        Args:
            countryCode (str | int): [if left as empty will return the global top ranks]
            
            brawler (str | int): [MUST HAVE INPUT]

        Returns:
            dict | str: [returns either an error with the error message and code or a dictionary of the top clubs]
        """
        
        if isinstance(countryCode,(str,int)) == False:
            raise Exception("Only a str or int type is allowed.")
        
        if isinstance(brawler,int) == False:
            raise Exception("Only a int type is allowed for brawler id, you can find it through get_brawlers() and find the id")
        
        if brawler == None:
            raise Exception("The brawler id must be entered, you can find it through get_brawlers() and find the id")
        
        countryCode = str(countryCode).replace("+","")
        response = requests.get(f"https://api.brawlstars.com/v1/rankings/{countryCode}/brawlers/{brawler}",headers=self.header)
        return self.handle_response(response=response)
    