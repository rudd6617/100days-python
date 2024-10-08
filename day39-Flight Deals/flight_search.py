import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.getenv("FLIGHT_API_KEY")
        self._api_secret = os.getenv("FLIGHT_API_SECRET")
        self._endpoint = os.getenv("FLIGHT_ENDPOINT")
        self._token = self._get_access_token()
        
    def _get_access_token(self):
        params = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret,
        }
        response = requests.post(
            url=f"{self._endpoint}/v1/security/oauth2/token", 
            data=params)
        
        return response.json()["access_token"]
        
    def get_destination_codes(self, city_name):
        headers = {
            "Authorization": f"Bearer {self._token}",
        }
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url=f"{self.endpoint}/v1/reference-data/locations/cities", 
            headers=headers, 
            params=query)
        
        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}")
            return "Not Found"
        
        return code
    
    def check_flights(self, from_airport, to_airport, from_date, return_date):
        headers = {
            "Authorization": f"Bearer {self._token}",
        }
        query = {
            "originLocationCode": from_airport,
            "destinationLocationCode": to_airport,
            "departureDate": from_date,
            "returnDate": return_date,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "USD",
            "max": 10,
        }
        
        response = requests.get(
            url=f"{self._endpoint}/v2/shopping/flight-offers", 
            headers=headers, 
            params=query)
        
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None
        
        return response.json()